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
    results = searchControl.searchResults(request.POST)
    