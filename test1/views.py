

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from test1.models import Product, Comment
from test1.serializers import ProductSerializer, CommentSerializer

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        new_product = ProductSerializer(data= request.data)
        if new_product.is_valid():
            new_product.save()
            return Response(new_product.data, status= status.HTTP_201_CREATED)
        return Response(new_product.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def product_detail(request,id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        productSerializer = ProductSerializer(product)
        comments = product.comment_set.all()
        commentsSerialize = CommentSerializer(comments, many = True)
        results = {
            'comments': commentsSerialize.data,
            'product' : productSerializer.data,
            'price' : productSerializer.data['price']
        }
        return Response(results)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
