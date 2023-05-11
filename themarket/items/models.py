from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        verbose_name_plural='Categories' #correction of django default spellings
        ordering=('name',) #alphabetical order
    def __str__(self):
        return self.name #categories called by names
class Item(models.Model):
        
        category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
        name=models.CharField(max_length=255)
        description=models.TextField(blank=True,null=True)
        price=models.FloatField(null=True)
        image=models.ImageField(upload_to='item_images',blank=True,null=True)
        is_sold=models.BooleanField(default=False)
        created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
        created_at=models.DateTimeField(auto_now_add=True)
        def __str__(self):
               return self.name