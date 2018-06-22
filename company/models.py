from django.db import models
from django.db.models import signals

status_choices = (
          ('Proposed','Proposed'),
          ('Contacted', 'Contacted'),
          ('Confirmed','Confirmed'),
)

category = (
('Regulator', 'Regulator'),
('Current client','Current client'),
('Prospective client','Prospective client'),
('Diplomatic Co.','Diplomatic Co.'),
('Mazars group','Mazars group'),
('Others','Others'),
)

class Invitees(models.Model):
    name = models.CharField(max_length=122)
    designation = models.CharField(max_length=122, blank=True, null=True)
    company = models.CharField(max_length=122, blank=True, null=True)
    status = models.CharField(choices= status_choices, max_length=122, blank=True, null=True)
    date_of_update = models.DateField(blank=True, null=True)
    telephone_contact = models.CharField(max_length=12,blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    comments = models.CharField(max_length=122, blank=True, null=True)
    category = models.CharField(choices=category, max_length=122, blank=True, null=True)

    def __str__(self):
        return self.name
