from django.shortcuts import render
from django.db import connection
from django.shortcuts import HttpResponse
from .models import *

# Create your views here.
def dashboard(request):

	cursor = connection.cursor()
	cursor.execute("""  select * from postgresdb_form """)
	for i in cursor.fetchall():
		print i
	cursor.close()	
	return HttpResponse("hiiii")	







