from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name':'Lets learn python!'},
    {'id':2, 'name':'Lets design!'},
    {'id':3, 'name':'Lets develop!'},
]

def home(request):
    context = {'rooms': room}    
    return render(request, 'base/home.html', context    )

def room(request):
    return render(request, 'room.html')