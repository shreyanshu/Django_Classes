"""demo_class6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from demo_app import urls as demo_app_url
from demo_app2 import urls as demo_app2_url
from django.conf.urls.static import static
from demo_class6 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('d1/', include(demo_app_url)),
    path('d2/', include(demo_app2_url))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)