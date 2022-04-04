from django.http import JsonResponse
from article.models import Article
from article.serializers import ArticleListSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# def article_list(request):
#     articles = Article.objects.all()
#     serializer = ArticleListSerializer(articles, many=True)
#     return JsonResponse(serializer.data, safe=False)


"""
1. DRF对视图的扩展应用
2. @api_view 装饰器允许视图接收 GET 、POST 请求，以及提供如 405 Method Not Allowed 等默认实现，以便在不同的请求下进行正确的响应。
返回了 Response ，该对象由 Django 原生响应体扩展而来，它可以根据内容协商来确定返回给客户端的正确内容类型。如果数据验证有误，还可以返回适当的状态码以表示当前的情况。
"""

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        artilces = Article.objects.all()
        serializer = ArticleListSerializer(artilces, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)