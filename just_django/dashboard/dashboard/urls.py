"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from news.views import *
from finance.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
 	url(r'^notes/', include('notepad.urls', namespace='notepad')),
 	url(r'^scrape/',scrape, name="scrape"),
    url(r'^home/',news_list, name="news_list"),
    url(r'^companies/',company_article_list, name="company_list"),
    url(r'^api/chart/data/',ChartData.as_view(), name="api-chart-data"),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
