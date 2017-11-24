import string
import random
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from accounts.models import *
import time
import datetime


def randon_string_generator(size, type=None):
    if type == "char":
        chars = chars = string.ascii_uppercase + string.ascii_lowercase
    elif type == "number":
        chars = string.digits
    return ''.join(random.choice(chars) for _ in range(size))

class Command(BaseCommand):

	form_data['name'] = randon_string_generator(12, 'char').title() 
	form_data['Email'] = randon_string_generator(12, 'char').title() 
	UserCategory.objects.create(**form_data)

	   
