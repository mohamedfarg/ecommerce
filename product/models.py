from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300, unique=True,db_index=True)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('product:product_search', args=[self.slug])
    

class Product(models.Model):
    title = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    discount = models.IntegerField(blank=True,null=True,default=0)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="product")
    track = models.CharField(max_length=255,blank=True)
    set_track = models.BooleanField(default=False,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    size = models.ManyToManyField("Color")
    color = models.ManyToManyField("Size")
    tags = models.ManyToManyField('Tag')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def set_on_track(self, track):
        self.set_track = True
        self.track = track
        self.save()
        
    def update_stock(self, quantity):
        self.stock -= quantity
        self.save()

    
    def get_url(self):
        return reverse('store:product_detail',args=[self.slug])

    class Meta:
        ordering = ('created',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.title)


class ProductComment(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.product}"

    class Meta:
        ordering = ['-created_at']
        


class Size(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) :
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) :
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) :
        return self.name
