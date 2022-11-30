from django.urls import path
from articles.views.article_views import ArticleList
from articles.views.product_views import CategoriesList
from articles.views.product_views import AttributesList
from articles.views.product_views import VariantsList
from articles.views.product_views import ProductsList

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('categories/', CategoriesList.as_view()),
    path('attributes/', AttributesList.as_view()),
    path('variants/', VariantsList.as_view()),
    path('products/', ProductsList.as_view())

]