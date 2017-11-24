import string
import random
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from form.models import UserCategory
from form.models import Dept

def random_string_generator(size, type=None):
    if type == "char":
        chars = chars = string.ascii_uppercase + string.ascii_lowercase
    elif type == "number":
        chars = string.digits
    return ''.join(random.choice(chars) for _ in range(size))

gender_list = {'Male' : 1, 'Female' : 2}
stName_list={'Andhra Pradesh':1,'Telangana':2}
dept_list= Dept.objects.all()
terms_list={'True':1,'False':2}     

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('no_anms', type=int)

    def handle(self, *args, **options):
        no_anms = options.get('no_anms')

        form_data={}
        for i in range(no_anms):          
            gender_choice = random.choice(gender_list.keys())
            state_choice = random.choice(stName_list.keys())
            dept_choice = random.choice(dept_list)
            terms_choice = random.choice(terms_list.keys())  

            form_data['name'] = random_string_generator(4, 'char').title() 
            userName = form_data['name']+"@gmail.com"
            form_data['Email'] = userName
            form_data['salary'] = random_string_generator(4, 'number')
            Tsalary=int(form_data['salary'])*0.1
            form_data['tds'] = Tsalary
            form_data['phone_number'] = random_string_generator(10, 'number')
            form_data['gender'] = gender_choice
            form_data['state'] = state_choice
            form_data['deptID'] = dept_choice
            form_data['status'] = terms_choice

            UserCategory.objects.create(**form_data)

       
