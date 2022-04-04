from pyexpat import model
from rest_framework import serializers
from article.models import Article


# 序列化, 优化前
# class ArticleListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(allow_blank=True, max_length=100)
#     body = serializers.CharField(allow_blank=True)
#     created = serializers.DateTimeField()
#     updated = serializers.DateTimeField()

# 序列化, 优化后, 父类变成ModelSerializer
class ArticleListSerializer(serializers.ModelSerializer):
    """
    自动推断需要序列化的字段及类型
    提供对字段数据的验证器的默认实现
    提供了修改数据需要用到的 .create() 、 .update() 方法的默认实现
    """
    class Meta:
        model = Article
        fields = [
            'created',
            'id',
            'title',

        ]