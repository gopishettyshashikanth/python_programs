from django.db import models

class userDetails(models.Model):
	file  = models.FileField(upload_to='documents/')    
    
