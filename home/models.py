from django.db import models
from django.urls import path,reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.CharField(max_length=200,unique=True)

    class Meta:
        ordering= ('name',)

        def __str__(self) -> str:
            self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products"),
    name=models.CharField(max_length=200)
    slug=models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created=models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering= ('name',)

    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse("home:product_detail",args=[self.slug])
    