from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_catalog = request.GET.get('sort')
    all_phones = Phone.objects.all()
    if sort_catalog == 'min_price':
        all_phones = all_phones.order_by('price')
    elif sort_catalog == 'max_price':
        all_phones = all_phones.order_by('-price')
    elif sort_catalog == 'name':
        all_phones = all_phones.order_by('name')
    context = {'phones': all_phones,
               }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)
