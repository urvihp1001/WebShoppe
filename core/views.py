from django.shortcuts import render,redirect
from items.models import Category, Item
from django.contrib.auth import logout
from .forms import SignupForm
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]#to get 6 unsold items to appear
    categories=Category.objects.all()
    return render(request,'core/index.html',{
        'categories':categories,
        'items':items,
        
    })
def contact(request):
    return render(request,'core/contact.html')
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            # print form errors to console for debugging
            print(form.errors)
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')
