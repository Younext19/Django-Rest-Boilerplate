from django.db import models
import uuid

class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=50)
    description = models.TextField(blank=False,null=False)
    slug = models.SlugField(max_length=50,blank= False)
    categories = models.ForeignKey('Categories',related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    img = models.URLField(max_length=255, blank=True, null=True)
    variants = models.ForeignKey('Variants',related_name='products', on_delete=models.DO_NOTHING,null=True,blank=True)
    class Meta:
        verbose_name = 'Product'
    def __str__(self):
        return str(self.nom)

class Categories(models.Model):
    nom = models.CharField(max_length=50)
    tax = models.DecimalField(max_digits=5,decimal_places=2,blank=True, null= True)
    show = models.BooleanField()
    class Meta:
        verbose_name = 'Categorie'
    def __str__(self):
        return str(self.nom)

class Variants(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    price = models.DecimalField(decimal_places=2,max_digits=19)
    barcode = models.CharField(max_length=30, blank=True,null=True)
    attribute = models.ForeignKey('Attributes', related_name='variants', on_delete=models.SET_NULL, null=True,blank=True)
    sku = models.CharField(max_length=10,blank=True,null=True)
    cost = models.CharField(max_length=20)
    def __str__(self):
        return str(self.id)
   

class Attributes(models.Model):
    src = models.URLField(null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.desc
