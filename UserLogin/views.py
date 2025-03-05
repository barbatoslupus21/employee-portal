from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from UserLogin.models import EmployeeLogin
from Profile.models import PersonalInformation

def is_personal_info_complete(personal_info):
    return all([
        personal_info.nickname,
        personal_info.gender,
        personal_info.birth_date,
        personal_info.birth_place,
        personal_info.contact_number,
        personal_info.mother,
        personal_info.father,
        personal_info.work_email,
        personal_info.present_street,
        personal_info.present_baranggay,
        personal_info.present_city,
        personal_info.present_province,
        personal_info.provincial_street,
        personal_info.provincial_baranggay,
        personal_info.provincial_city,
        personal_info.provincial_province,
        personal_info.contact_firstname,
        personal_info.contact_lastname,
        personal_info.contact_relation,
        personal_info.contact_no,
        personal_info.contact_street,
        personal_info.contact_baranggay,
        personal_info.contact_city,
        personal_info.contact_province,
        personal_info.primary_school,
        personal_info.secondary_school,
        personal_info.vocational_school,
        personal_info.tertiary_school,
    ])

def login_view(request):
    if request.user.is_authenticated:
        return redirect('Dashboard:Dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = EmployeeLogin.objects.get(username=username)
        except EmployeeLogin.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return render(request, 'UserLogin/loginpage.html', {'page': 'login'})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_approved == "For Approval":
                messages.error(request, 'Your account is currently under the approval process.')
                return render(request, 'UserLogin/loginpage.html', {'page': 'login'})
            
            elif user.is_approved == "Disapproved":
                messages.error(request, 'Your account has been disapproved.')
                return render(request, 'UserLogin/loginpage.html', {'page': 'login'})
            
            elif user.is_locked:
                messages.error(request, 'Your account access has been temporarily locked. Please contact the HR department to regain access.')
                return render(request, 'UserLogin/loginpage.html', {'page': 'login'})
            
            elif user.is_approved == "Approved":
                login(request, user)
                personal_info = PersonalInformation.objects.filter(name=user).first()
                if user.is_admin:
                    return redirect('Dashboard:admin-dashboard')

                if personal_info is None or not is_personal_info_complete(personal_info):
                    return redirect('edit-profile')

                
                return redirect('Dashboard:Dashboard')
        else:
            messages.error(request, 'Login credentials are incorrect.')
    
    return render(request, 'UserLogin/loginpage.html', {'page': 'login'})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        idnumber = request.POST.get('idnumber')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        name = f"{firstname} {lastname}"
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm-password')

        if password1 == password2:
            if EmployeeLogin.objects.filter(username=username).exists():
                messages.error(request, 'ID Number already exists!')
            elif EmployeeLogin.objects.filter(idnumber=idnumber).exists():
                messages.error(request, 'Id number already exists!')
            elif EmployeeLogin.objects.filter(email=email).exists():
                messages.error(request, 'Email address already exists!')
            else:
                user = EmployeeLogin.objects.create_user(username=username, idnumber=idnumber, firstname=firstname, lastname=lastname, name=name, email=email, password=password1)
                user.set_password(password1)
                user.save()
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'UserLogin/registerpage.html')