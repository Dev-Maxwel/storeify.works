from django.shortcuts import render, redirect
from .models import imageControls, searchControl
from .forms import EmailMarketingForm

# Create your views here.

def index(request):
    images = imageControls.objects.all()
    context={
        images: "images"
    }
    return render(request, "store1/index.html", context)

def catalogue(request):
    images = imageControls.objects.all()
    context={
        images: "images"
    }
    return render(request, "store1/catalogue.html", context)

def success(request):
    if request.method == 'POST':
        form = EmailMarketingForm(request.POST)
        if form.is_valid():
            form.save()
            print('Email has been saved')
            # Redirect after capturing email
            return redirect('success')
        else:
            print('Form is not valid:', form.errors)
    else:      
        form = EmailMarketingForm()
        
    context = {'form': form}
    return render(request, 'store1/success.html', context)

def search(request):
    searchQuery = request.GET.get('q', '')
    # results = searchControl.searchResults(request.POST) 
    
    #temporary testresults
    # results = imageControls.description1
    results= imageControls.objects.filter().order_by("?")
    context = {
        results: "results",     
    }
    return render(request, "store1/results.html", context)

def signin(request):
    if request.method == "POST":
        email = request.post.get('email')
        password = request.post.get('password')
    else:
        pass    
    return render (request, "shared/signin.html")

    