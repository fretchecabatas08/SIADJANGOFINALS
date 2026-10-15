from django.shortcuts import render, get_object_or_404, redirect
from .models import LostFoundItem
from .forms import LostFoundItemForm

def index(request):
    items = LostFoundItem.objects.all().order_by('-date_reported')

    total_items = items.count()
    lost_items = items.filter(lost_found_status='Lost').count()
    found_items = items.filter(lost_found_status='Found').count()
    claimed_items = items.filter(item_status='Claimed').count()

    context = {
        'items': items,
        'total_items': total_items,
        'lost_items': lost_items,
        'found_items': found_items,
        'claimed_items': claimed_items,
    }

    return render(request, 'chay_id/index.html', context)


def add_item(request):
    if request.method == 'POST':
        item_data = {
            'item_name': request.POST.get('item_name'),
            'description': request.POST.get('description'),
            'category': request.POST.get('category'),
            'lost_found_status': request.POST.get('lost_found_status'),
            'date_reported': request.POST.get('date_reported'),
            'location': request.POST.get('location'),
            'color': request.POST.get('color'),
            'reporter_name': request.POST.get('reporter_name'),
            'contact_information': request.POST.get('contact_information'),
            'item_status': request.POST.get('item_status'),
        }

        new_photo = request.FILES.get('item_photo')
        if new_photo:
            item_data['item_photo'] = new_photo

        LostFoundItem.objects.create(**item_data)
        return redirect('index')

    return render(request, 'chay_id/add_item.html')


def item_detail(request, item_id):
    item = get_object_or_404(LostFoundItem, id=item_id)
    return render(request, 'chay_id/item_detail.html', {'item': item})


def edit_item(request, item_id):
    item = get_object_or_404(LostFoundItem, id=item_id)
    form_data = request.POST if request.method == 'POST' else None
    form = LostFoundItemForm(form_data, instance=item)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('item_detail', item_id=item.id)

    return render(request, 'chay_id/edit_item.html', {'item': item, 'form': form})


def delete_item(request, item_id):
    item = get_object_or_404(LostFoundItem, id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('index')

    return render(request, 'chay_id/delete_item.html', {'item': item})