from django.db import models
from django.urls import reverse
# Create your models here.



class category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    img=models.ImageField(upload_to="category",blank=True)

    class Meta:
        ordering=("name",)
        verbose_name="category"
        verbose_name_plural="categories"

    def get_url(self):
        return reverse("shoppingapp:product_by_category",args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    img=models.ImageField(upload_to="product",blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse("shoppingapp:prodcatdetail",args=[self.category.slug,self.slug])

    class Meta:
        ordering=("name",)
        verbose_name="product"
        verbose_name_plural="products"

    def __str__(self):
        return '{}'.format(self.name)



