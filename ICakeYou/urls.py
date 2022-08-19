"""ICakeYou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

from ICY.views import ProductsView, ProductView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cache_page(60)(ProductsView.as_view())),
    path('products/<int:pk>', cache_page(60)(ProductView.as_view()), name='product'),
    # path('', ProductsView.as_view()),
    # path('products/<int:pk>', ProductView.as_view(), name='product'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
