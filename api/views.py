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

    def delete(self, request, pk):
        produto = Produto.objects.get(id=pk)
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        produto = Produto.objects.get(id=pk)
        serializer = ProdutoSerializer(produto, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["post"],detail=False,url_path="purchase")
    def purchase(self, request, pk=None):
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity"))
        produto = Produto.objects.get(id=product_id)
        send_mail.apply_async(args=[produto.id])
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