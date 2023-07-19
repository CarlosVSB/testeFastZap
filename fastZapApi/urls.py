from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api.views import ProdutoViewSet

router = routers.DefaultRouter()

# GET: produto/ | POST: produto/ + JSON | PUT: produto/<id>/ + JSON | DELETE: produto/<id>/
router.register(r'produto', ProdutoViewSet, basename='produto')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('produto/purchase/', ProdutoViewSet.as_view({"post": "purchase"})),
    path('api-auth/', include('rest_framework.urls'))
]
