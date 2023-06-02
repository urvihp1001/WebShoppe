from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from items.models import Item
@login_required
def index(request):
    items = Item.objects.for_user(request.user)
    return render(request, 'dashboard/index.html', {
        'items': items,
    })


    
