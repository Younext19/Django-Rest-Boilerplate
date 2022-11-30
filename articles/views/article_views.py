from django.shortcuts import render
from rest_framework.views import APIView
from articles.models.article_models import Article
from articles.serializers.article_serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ArticleList(APIView):

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Bad Req", status=status.HTTP_400_BAD_REQUEST)
