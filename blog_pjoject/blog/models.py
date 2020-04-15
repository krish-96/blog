from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=264, blank=False, null=False)
    body = models.TextField(max_length=2000, blank=False, null=False)