from django.shortcuts import render

# Create your views here.
count=0
def index(request):
    return render(request,"example/index.html",{
        "count":count
    })