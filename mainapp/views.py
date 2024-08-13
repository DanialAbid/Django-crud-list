from django.shortcuts import render, redirect, get_object_or_404
from .models import product, category
import os

def index(request):
    products = product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        cate = request.POST['cate']
        pname = request.POST['pname']
        pprice = request.POST['pprice']
        pq = request.POST['pq']
        pi = request.FILES.get('pi')
        categ = get_object_or_404(category, categoryname=cate)
        product.objects.create(category=categ, pprice=pprice, pname=pname, pimage=pi, quantity=pq)
        return redirect('create')  
    cates = category.objects.all()
    return render(request, 'create.html',{'cates':cates})

def create_cate(request):
    if request.method == 'POST':
        cname = request.POST['catename']
        featured = request.POST.get('featured')
        if featured == 'on':
            category.objects.create(categoryname=cname,is_featured=True)
        else:
            category.objects.create(categoryname=cname,is_featured=False)
        return redirect('createcate')
    return render(request,'addcate.html')

def edit(request, id):
    prod = get_object_or_404(product, pk=id)  
    if request.method == 'POST':
        cate = request.POST['cate']
        pname = request.POST['pname']
        pprice = request.POST['pprice']
        pq = request.POST['pq']
        pi = request.FILES.get('pi')

        
        categ = get_object_or_404(category, categoryname=cate)
        
        
        prod.category = categ
        prod.pname = pname
        prod.pprice = pprice
        prod.quantity = pq

        
        if pi:
            prod.pimage = pi

        prod.save()  
        return redirect('index')  

    categories = category.objects.all() 
    return render(request, 'edit.html', {'prod': prod, 'categories': categories})







def delete(request, pk):
    prod = get_object_or_404(product, pk=pk)  

    if len(prod.pimage) > 0:
        os.remove(prod.pimage.path)
    if request.method == 'POST':
        prod.delete()  
        return redirect('index')  
   
    return render(request, 'index.html', {'prod': prod})
