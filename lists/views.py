from django.shortcuts import render
from lists.models import Item

def home_page(request):
    new_item_text = ''
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text) #substitui Item.save()
    
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
