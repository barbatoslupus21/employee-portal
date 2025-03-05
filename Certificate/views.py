from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from UserLogin.models import EmployeeLogin
from .models import Certificate, CertificateList, CertSpeaker, Awardees, SigningAuthority
import json
from Notification.models import Notification
from django.contrib import messages
from Profile.models import EmploymentInformation
from django.http import HttpResponseRedirect, HttpResponse
import base64
import json
import logging
from django.core.files.base import ContentFile
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def admin_certificate(request):
    templates = Certificate.objects.all()
    certificates = CertificateList.objects.all().order_by("-posted_at")
    awardees = EmployeeLogin.objects.filter(is_active=True).exclude(is_admin=True)
    speakers = CertSpeaker.objects.all()
    context={\
        'templates':templates,
        'certificates':certificates,
        'awardees':awardees,
        'speakers':speakers
    }
    return render(request, 'Certificate/admin-certificate.html', context)

@login_required(login_url='login')
def create_certificate(request):
    if request.method == 'POST':
        template = request.POST.get('template')
        cert_temp = Certificate.objects.get(title=template)

        speaker = request.POST.get('speaker')
        cert_speaker = CertSpeaker.objects.get(name=speaker)

        CertificateForm = CertificateList.objects.create(
            cert_date=request.POST['certificate_date'],
            cert_name=request.POST['certificate_name'],
            cert_template=cert_temp,
            cert_speaker=cert_speaker
        )

        selected_participants = json.loads(request.POST['selected_participants'])

        for participant_id in selected_participants:
            employee = EmployeeLogin.objects.get(idnumber=participant_id)
            Awardees.objects.create(
                awardeee=employee,
                certificate=CertificateForm
            )

            Notification.objects.create(
                level="Medium",
                module="Certificate",
                notifier=request.user,
                page="certificate",
                reciever=employee,
                message="has given you a certificate."
            )

        return redirect('admin-certificate')

    awardees = EmployeeLogin.objects.filter(is_active=True).exclude(is_admin=True)
    return render(request, 'Certificate/admin-certiticate.html', {'awardees': awardees})

@login_required(login_url='login')
def delete_certificate(request, pk):
    deleteCert = get_object_or_404(CertificateList, id=pk)

    if request.method == "POST":
        deleteCert.delete()
        messages.success(request, 'Certificate deleted.')
        return redirect('admin-certificate')
    else:
        messages.error(request, 'Invalid request method.')
    return redirect('admin-certificate')

@login_required(login_url='login')
def awardees_view(request, pk):
    certificate = CertificateList.objects.get(id=pk)
    awardees = Awardees.objects.filter(certificate=pk)
    approvers = SigningAuthority.objects.filter(certificate=certificate.cert_template)
    for awardee in awardees:
        try:
            awardee_department = EmploymentInformation.objects.filter(name=awardee.awardeee).first()
            if awardee_department:
                awardee.department = awardee_department.department.abreviation
            else:
                awardee.department = None
                
            awardee_line = EmploymentInformation.objects.filter(name=awardee.awardeee).first()
            if awardee_line:
                awardee.line = awardee_line.line.line
            else:
                awardee.line = None
        except EmploymentInformation.DoesNotExist:
            request.department = None
            request.line = None

    context={
        'awardees':awardees,
        'certificate':certificate,
        'approvers':approvers
    }
    return render(request, 'Certificate/admin-view-awardees.html', context)

@login_required(login_url='login')
def delete_awardee(request, pk):
    deleteAwardee = get_object_or_404(Awardees, id=pk)
    
    if request.method == "POST":
        deleteAwardee.delete()
        messages.success(request, 'Awardee deleted.')
    else:
        messages.error(request, 'Invalid request method.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='login')
def certificate_view(request):
    certificates = Awardees.objects.filter(awardeee=request.user)
    for certificate in certificates:
        try:
            certificates_approvers = SigningAuthority.objects.filter(certificate=certificate.certificate.cert_template)
            if certificates_approvers:
                certificate.approvers = certificates_approvers
            else:
                certificate.approvers = None
        except SigningAuthority.DoesNotExist:
            certificate.approvers = None
    context={
        'certificates':certificates
    }
    return render(request, 'Certificate/certificate.html', context)

logger = logging.getLogger(__name__)

@login_required(login_url='login')
def send_certificate(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            required_fields = ['image', 'recipient', 'cert_type', 'cert_name', 'cert_date', 'recipient_name']
            if not all(field in data for field in required_fields):
                return HttpResponse('Missing fields in the request data', status=400)

            subject = f"Your {data['cert_type']} Certificate: {data['cert_name']}"
            recipient_name = data['recipient_name']
            cert_type = data['cert_type']
            cert_name = data['cert_name']

            body = (
                f"Hello {recipient_name},\n\n"
                f"Please find your Certificate of {cert_type} attached to this email.\n\n"
                f"We congratulate you on your achievement and thank you for being a part of {cert_name}.\n\n"
                "Sincerely,\n\n"
                "HR Department\n"
                "Ryonan Electric Philippines Corporation"
            )

            email = EmailMessage(subject, body, 'fadpayslip1995@gmail.com', [data['recipient']])

            image_data = data['image']
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]
            img_data = base64.b64decode(imgstr)

            image_file = ContentFile(img_data, name=f'certificate.{ext}')
            email.attach(f'certificate.{ext}', image_file.read(), f'image/{ext}')

            email.send()

            return HttpResponse('Certificate sent successfully!')
        except json.JSONDecodeError:
            return HttpResponse('Invalid JSON', status=400)
        except Exception as e:
            return HttpResponse(f'Error sending email: {str(e)}', status=500) 
    return HttpResponse('Invalid request method', status=405)

