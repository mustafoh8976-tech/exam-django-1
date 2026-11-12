from django.shortcuts import render
from .models import *

def home_view(request):
    return render(request,'home.html')



def create_autor(request):
    context = {'first_n': '', 'last_n': '', 'age': '', 'country': ''}
    if request.method == 'POST':
        first_n = request.POST.get('first_n')
        last_n = request.POST.get('last_n')
        age = request.POST.get('age')
        country = request.POST.get('country')
        context = {'first_n': first_n, 'last_n': last_n, 'age': age, 'country': country}
    return render(request, 'create_autor.html', context=context)



def delete_autor(request,pk):
    autor = Auter.objects.get(pk=pk)
    autor.delete()
    return render(request,'delete_autor.html')



def update_autor(request,pk):
    autor = Auter.objects.get(pk=pk)
    if request.method == 'POST':
        autor.first_n = request.POST.get('first_n')
        autor.last_n = request.POST.get('last_n')
        autor.age = request.POST.get('age')
        autor.country = request.POST.get('country') 
        return render(request,'update_autor.html',context={'first_n':autor.first_n,'last_n':autor.last_n,'age':autor.age,'country':autor.country})
    return render(request,'update_autor.html',context={'first_n':autor.first_n,'last_n':autor.last_n,'age':autor.age,'country':autor.country})



def list_autor(request):
    autors = Auter.objects.all()
    return render(request,'list_autor.html',context={'autors':autors})
    
    
    
def create_book(request):
    context = {'name_b': '', 'pablisher': '', 'create_at': '', 'create_autor_at': ''}
    if request.method == 'POST':
        name_b = request.POST.get('name_b')
        pablisher = request.POST.get('pablisher')
        create_at = request.POST.get('create_at')
        create_autor_at = request.POST.get('create_autor_at')
        context = {'name_b': name_b, 'pablisher': pablisher, 'create_at': create_at, 'create_autor_at': create_autor_at}
    return render(request, 'create_book.html', context=context)
    


def delete_book(request,pk):
    book = Books.objects.get(pk=pk)
    book.delete()
    return render(request,'delete_book.html')  
    
    
    
def update_book(request,pk):
    book = Books.objects.get(pk=pk)
    if request.method == 'POST':
        book.name_b = request.POST.get('name_b')
        book.pablisher = request.POST.get('pablisher')
        book.create_at = request.POST.get('create_at')
        book.create_autor_at = request.POST.get('create_autor_at') 
        return render(request,'update_book.html',context={'name_b':book.name_b,'pablisher':book.pablisher,'create_at':book.create_at,'create_autor_at':book.create_autor_at})
    return render(request,'update_book.html',context={'name_b':book.name_b,'pablisher':book.pablisher,'create_at':book.create_at,'create_autor_at':book.create_autor_at})
    
    
      
def list_book(request):
    books = Books.objects.all()
    return render(request,'list_book.html',context={'books':books})   



def create_order(request):
    context = {'booK_id': '', 'quantity_day': '', 'first_p': '', 'last_p': '', 'username': ''}
    if request.method == 'POST':
        booK_id = request.POST.get('booK_id')
        quantity_day = request.POST.get('quantity_day')
        first_p = request.POST.get('first_p')
        last_p = request.POST.get('last_p')
        username = request.POST.get('username')
        context = {'booK_id': booK_id, 'quantity_day': quantity_day, 'first_p': first_p, 'last_p': last_p, 'username': username}
    return render(request, 'create_order.html', context=context)
    
  
    
def delete_order(request,pk): 
    order = Order.objects.get(pk=pk)
    order.delete()
    return render(request,'delete_order.html') 
    
    
    
def update_order(request,pk): 
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.booK_id = request.POST.get('booK_id')
        order.quantity_day = request.POST.get('quantity_day')
        order.first_p = request.POST.get('first_p')
        order.last_p = request.POST.get('last_p') 
        order.username = request.POST.get('username')
        return render(request,'update_order.html',context={'booK_id':order.booK_id_id,'quantity_day':order.quantity_day,'first_p':order.first_p,'last_p':order.last_p,'username':order.username})
    return render(request,'update_order.html',context={'booK_id':order.booK_id_id,'quantity_day':order.quantity_day,'first_p':order.first_p,'last_p':order.last_p,'username':order.username})
    
   
    
def list_order(request): 
    orders = Order.objects.all()
    return render(request,'list_order.html',context={'orders':orders})