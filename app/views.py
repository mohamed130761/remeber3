from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'pages/home.html')
def about(request):
    return render(request,'pages/about.html')
def navbar(request):
    return render(request,'parts/navbar.html')
def footer(request):
    return render(request,'parts/footer.html')
def contact(request):
    return render(request,'pages/contact.html')