from django.http import HttpResponse
from django.shortcuts import render


# models.py, admin.py, views.py, urls.py

# def home_page(request):
#     return HttpResponse("<h1>Hello</h1>")
from products.forms import FormModelForm
from products.models import ProductModel


def index_page(request):
    # products = ProductModel.objects.all().filter(title__icontains="Iphone12")
    # products = ProductModel.objects.all().order_by('-id')

    return render(request, 'index.html', )


def shop_page(request):
    products = ProductModel.objects.all()
    return render(request, 'shop.html', {'products': products})

# context ={}
#
#     # add the dictionary during initialization
#     form = GeeksForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#     context['form']= form
#     return render(request, "create_view.html", context)
def send_form(request):
    context = {}

    form = FormModelForm(request.POST)
    if form.is_valid():
        form.save()

    context['blabla'] = form
    return render(request, 'forms.html', context)
