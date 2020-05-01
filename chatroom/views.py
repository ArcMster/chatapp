from django.shortcuts import render
from django.http import HttpResponse
from .models import Messages

# Create your views here.
def home(request):
    all_messages = Messages.objects.all()
    msg_list = []
    for i in all_messages:
        msg_list.append(i)
    return render(request,'page.html',{"message":msg_list})

'''def store_message(request):
    message = request.POST['message']
    new_message = Messages()
    new_message.message = message
    new_message.save()

    
    return render(request,'message_fetch.html')'''

def store_message(request):
    message = request.POST['message']
    name = request.POST['name']
    new_message = Messages()
    new_message.message = message
    new_message.name = name
    new_message.save()

    all_messages = Messages.objects.all()
    msg_list = []
    for i in all_messages:
        msg_list.append(i)
    print(msg_list)
    
    return render(request,'page.html',{"message":msg_list})

def message_fetch(request):
    all_messages = Messages.objects.all()
    msg_list = []
    for i in all_messages:
        msg_list.append(i.message)
    print(msg_list)
    
    return render(request,'messages.html',{"message":msg_list})