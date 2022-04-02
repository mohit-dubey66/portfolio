import email
from django.http import HttpResponse
from django.shortcuts import render

from home.models import Contact

# Create your views here.
def index(request):
    if request.method == 'POST':
        fullName = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contactDetails = Contact(fullName = fullName, email = email, message = message)
        contactDetails.save() 
    return render(request, 'index.html')

def projects(request):
    return HttpResponse("Projects Loading...")