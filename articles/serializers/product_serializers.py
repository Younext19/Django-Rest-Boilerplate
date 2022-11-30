from rest_framework import serializers
from articles.models.product_models import Categories, Variants, Attributes, Products

class GetCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id','nom','tax','show']

class PostCategoriesSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Categories
        fields = ['nom','tax','show']

class PutCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ['tax','show']

    

class GetAttributes(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ['id','src','desc']

class PostAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ['src','desc']


class PutAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ['src','desc']
        


    
class GetVariantsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Variants
        fields = ['id','price','barcode','attribute','sku','cost']
    
class PostVariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variants
        fields = ['price','barcode','attribute','sku','cost']


        
class GetProductsSerializer(serializers.ModelSerializer):
    variants = GetVariantsSerializer()
    categories = GetCategoriesSerializer()
    class Meta:
        model = Products
        fields = ['id','nom','description','categories','img','variants']
    