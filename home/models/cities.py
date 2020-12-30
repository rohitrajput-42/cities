from django.db import models

class Cities(models.Model):

    img = models.ImageField(upload_to = 'pics')
    title = models.CharField(max_length = 150) 
    desc = models.CharField(max_length = 15000)