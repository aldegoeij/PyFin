from django.db import models

class AuditLog(models.Model): #FIXME
    """
    This class defines the project wide audit log database model
    """
    def __unicode__(self):
        return self.action

    timestamp = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    action_type = models.CharField(max_length=200)
    action = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    result = models.IntegerField(max_length=200, choices=((0,'blocked'),(1, 'allowed'), (-1,'error')))