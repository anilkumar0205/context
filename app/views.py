from django.shortcuts import render

# Create your views here.

def zack(request):
    assumption='this data is writeen by the backend using context '
    d={'data':assumption}

    return render(request,'zack.html',d)
