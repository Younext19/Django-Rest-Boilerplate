from rest_framework import serializers
from articles.models.article_models import Article
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','Medicament','description','imgLinkAddress','created']

