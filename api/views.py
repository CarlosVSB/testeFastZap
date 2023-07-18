import time

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from fastZapApi.celery import app

from .models import Produto
from .serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    # http_method_names = ['get', 'post', 'head', 'delete', 'put']

    # def get_queryset(self):
    #     send_mail.apply_async(args=[1])
    #     print("ABCDEFG")
    #     return Produto.objects.all()
    
    # def list(self, request):
    #     print("ABCDEFG")
    #     send_mail.apply_async(args=[1])
    #     queryset = Produto.objects.all()
    #     serializer = ProdutoSerializer(queryset, many=True)
    #     return Response(serializer.data)

    def delete(self, request, pk):
        produto = Produto.objects.get(id=pk)
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        produto = Produto.objects.get(id=pk)
        send_mail.apply_async(args=[produto.id])
        serializer = ProdutoSerializer(produto, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def purchase(self, request, pk=None):
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity")
        produto = Produto.objects.get(id=product_id)
        if produto.quantity >= quantity:
            produto.quantity -= quantity
            produto.save()
            return HttpResponse("Venda realizada com sucesso!")
        else:
            raise ValidationError


@app.task(bind=True)
def send_mail(task_definition, produto_id):
    # time.sleep(5)
    time.sleep(5)
    print(f"E-mail enviado para o produto com ID {produto_id}")