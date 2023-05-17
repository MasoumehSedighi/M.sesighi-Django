from django.shortcuts import render

# Create your views here.

def indexView(request):
    context = {"name":"Mary"}
    return render(request,"index.html", context)
