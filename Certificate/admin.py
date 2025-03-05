from django.contrib import admin
from .models import Certificate, CertificateList, CertSpeaker, Awardees, SigningAuthority

admin.site.register(Certificate)
admin.site.register(CertificateList)
admin.site.register(CertSpeaker)
admin.site.register(Awardees)
admin.site.register(SigningAuthority)