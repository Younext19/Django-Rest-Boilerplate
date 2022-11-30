from django.contrib import admin
from articles.models.article_models import Article
from articles.models.product_models import Products
from articles.models.product_models import Categories
from articles.models.product_models import Attributes
from articles.models.product_models import Variants


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Article,AuthorAdmin)
admin.site.register(Categories,AuthorAdmin)
admin.site.register(Products,AuthorAdmin)
admin.site.register(Attributes, AuthorAdmin)
admin.site.register(Variants, AuthorAdmin)