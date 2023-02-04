from django.db import models

class MenuCategory(models.Model):
    menu_category_name=models.CharField(max_length=200)

class Menu(models.Model):
    menu_itm=models.CharField(max_length=100)
    price=models.IntegerField(null=False)
    category_id=models.ForeignKey(MenuCategory,on_delete=models.PROTECT,default=None,related_name='category_name')

class  DrinksCategory(models.Model):
    category_name=models.CharField(max_length=200)

class Drinks(models.Model):
    drink=models.CharField(max_length=200)
    price=models.IntegerField()
    category_id=models.ForeignKey(DrinksCategory,on_delete=models.PROTECT,default=None)



<<<<<<< HEAD
    
=======
>>>>>>> a89c04b44cadc735b6469291e38ffd92c5dce916
