from django.db import models

    
    
class Books(models.Model):
    name_b = models.CharField(max_length=200)
    pablisher = models.CharField(max_length=150)
    create_at = models.DateField()
    create_autor_at = models.IntegerField()
    
    
class Auter(models.Model):
    first_n = models.CharField(max_length=150)
    last_n = models.CharField(max_length=150)
    country = models.CharField(max_length=120)
    age = models.IntegerField()
    books = models.ManyToManyField(Books,related_name='auter')
    
    
    
    
class Order(models.Model):
    booK_id = models.ForeignKey(Books,on_delete=models.CASCADE)
    quantity_day = models.IntegerField()
    first_p = models.CharField(max_length=150)
    last_p = models.CharField(max_length=150)
    username = models.CharField(max_length=200,unique=True)
    
    
    
    