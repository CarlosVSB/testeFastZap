# APIFastZap
Teste para empresa FastZap que inclui a criação de uma API com Django

# Teste FastZap

## 1 - Para executar dentro do docker

### Preparando o ambiente
### Primeiro precisamos garantir que o dispositivo consiga criar um ambiente e que tenha o docker instalado

```
sudo apt-get install python3-venv
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose
```

### Buildar a aplicação

```
docker-compose build (Em alguns casos necessita permissões de super usuário)
```

### Subir a imagem para no Docker

```
docker-compose up -d (Em alguns casos necessita permissões de super usuário)
```

## 2 - Informações de uso

####  Formato json para criar produtos

```
Exemplo JSON:
  
{
  "name": "Nome do produto",
  "description": "Descrição do produto",
  "price": "8.99",
  "quantity": "8"
}
```

#### Para realizar vendas

```
O formato da rota de venda é: "produto/purchase/"

Exemplo JSON para uma venda

{
  "product_id": "ID do produto em questão",
  "quantity": "5"
}
```



