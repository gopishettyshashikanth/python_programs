from django.db import models

class fileupload(models.Model):
	file  = models.FileField(upload_to='documents/')    
    
class userDetails(models.Model):
	name = models.CharField(max_length=50)
	location = models.CharField(max_length=50)

class details(models.Model):
	name = models.CharField(max_length=80,null=True,blank=True)
	s_w_d_of = models.CharField(max_length=80,null=True,blank=True)
	gender = models.CharField(max_length=80,null=True,blank=True)

	caste = models.CharField(max_length=80,null=True,blank=True)
	dno = models.CharField(max_length=80,null=True,blank=True)
	street = models.CharField(max_length=80,null=True,blank=True)

	colony = models.CharField(max_length=80,null=True,blank=True)
	village = models.CharField(max_length=80,null=True,blank=True)
	pincode = models.CharField(max_length=80,null=True,blank=True)

	mandal = models.CharField(max_length=80,null=True,blank=True)
	assembly_code = models.CharField(max_length=80,null=True,blank=True)
	membership_id = models.CharField(max_length=80,null=True,blank=True)

	active_membership_id = models.CharField(max_length=80,null=True,blank=True)
	mobile_number = models.CharField(max_length=80,null=True,blank=True)
	email = models.CharField(max_length=80,null=True,blank=True)

	amount = models.CharField(max_length=80,null=True,blank=True)
	remark = models.CharField(max_length=80,null=True,blank=True)