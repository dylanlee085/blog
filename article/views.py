from re import A
from django.http import JsonResponse
from article.models import Article
from article.serializers import ArticleListSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.http import Http404
from article.models import Article

from article.serializers import ArticleDetailSerializer




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


"""
序列化器 serializer 不仅可以将数据进行序列化、反序列化，还包含数据验证、错误处理、数据库操作等能力。
"""
class ArticleDetail(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article, data=request.data)
        # 验证提交的数据是否合法
        # 不合法则返回400
        if serializer.is_valid():
            # 序列化器将持有的数据反序列化后，
            # 保存到数据库中
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        # 删除成功后返回204
        return Response(status=status.HTTP_204_NO_CONTENT)