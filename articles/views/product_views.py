from django.shortcuts import render
from rest_framework.views import APIView
from articles.models.product_models import Categories,Variants, Attributes, Products
from articles.serializers.product_serializers import GetCategoriesSerializer, PutCategoriesSerializer, PostCategoriesSerializer, GetAttributes, PostAttributesSerializer,PutAttributesSerializer, GetVariantsSerializer, PostVariantsSerializer, GetProductsSerializer
from rest_framework.response import Response
from rest_framework import status

class CategoriesList(APIView):

    def get(self, request, format=None):
        categories = Categories.objects.all()
        serializer = GetCategoriesSerializer(categories,many = True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = PostCategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Bad Req", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        cat_id = request.data['id']
        categorie = Categories.objects.get(id=cat_id)
        serializer = PutCategoriesSerializer(categorie, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        data = request.data
        categories_id = request.data['id']
        categories = Categories.objects.get(id=categories_id)
        if categories:
            categories.delete()
            return Response({"Details": "Category Deleted successfully."}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AttributesList(APIView):
    def get(self,request, format=None):
        attributes = Attributes.objects.all()
        serializer = GetAttributes(attributes,many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostAttributesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Bad Req", status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, format=None):
        attr_id = request.data['id']
        attributes = Attributes.objects.get(id=attr_id)
        serializer = PutAttributesSerializer(attributes, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        attr_id = request.data['id']
        attributes = Attributes.objects.get(id=attr_id)
        if attributes:
            attributes.delete()
            return Response({"Details": "Attribute Deleted successfully."}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)




class VariantsList(APIView):
    def get(self,request, format=None):
        variants = Variants.objects.all()
        serializer = GetVariantsSerializer(variants,many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostVariantsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Bad Req", status=status.HTTP_400_BAD_REQUEST)
    # def put(self, request, format=None):
    #     attr_id = request.data['id']
    #     attributes = Attributes.objects.get(id=attr_id)
    #     serializer = PutAttributesSerializer(attributes, data=request.data, partial=True)
        
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, format=None):
    #     attr_id = request.data['id']
    #     attributes = Attributes.objects.get(id=attr_id)
    #     if attributes:
    #         attributes.delete()
    #         return Response({"Details": "Attribute Deleted successfully."}, status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)


        
class ProductsList(APIView):

    def get(self, request, format=None):
        products = Products.objects.all()
        serializer = GetProductsSerializer(products,many = True)
        return Response(serializer.data)