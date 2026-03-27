from django.shortcuts import render,redirect
from .forms import ContactEnthusiastsForm
# Create your views here.

def home(request):
    return render(request , 'index.html')
    
def signup(request):
    if request.method == "POST":
        form = ContactEnthusiastsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirect back to homepage
    else:
        form = ContactEnthusiastsForm()
    
    return render(request, 'form.html', {'form': form})