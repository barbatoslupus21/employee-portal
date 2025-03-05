from django.db import models
from UserLogin.models import EmployeeLogin

class CertSpeaker(models.Model):
    name = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    signature = models.ImageField(upload_to='signatures/', blank=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    certificate_type = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=100, null=True)
    template = models.ImageField(upload_to='cert-template/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SigningAuthority(models.Model):
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    approver = models.ForeignKey(CertSpeaker, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.certificate.title} - {self.approver.name}'

class CertificateList(models.Model):
    cert_date = models.DateField()
    cert_name = models.CharField(max_length=100, null=True)
    cert_template = models.ForeignKey(Certificate, on_delete=models.CASCADE, null=True)
    cert_speaker = models.ForeignKey(CertSpeaker, on_delete=models.CASCADE, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.cert_name
    
class Awardees(models.Model):
    awardeee = models.ForeignKey(EmployeeLogin, on_delete=models.CASCADE, related_name='awardees')
    certificate = models.ForeignKey(CertificateList, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.awardeee.name} - {self.certificate}'