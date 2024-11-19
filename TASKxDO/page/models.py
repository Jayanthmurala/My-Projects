from django.db import models

# Create your models here.
class To_do_data(models.Model):
    task_name=models.CharField(max_length=255)
    task_details=models.TextField(null=True, blank=True)
    target_time=models.DateTimeField(null=True, blank=True)
    uploded_on=models.DateTimeField(auto_now=True)
    upgrade_on=models.DateTimeField(auto_now_add=True)
    