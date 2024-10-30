"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.get_all,name='get'),
    path('add',views.add_user,name='add'),
    path('delete/<int:pk>',views.delete_user,name='dlt_user'),
    path('update/<int:pk>',views.update,name='update_user'),
    path('k',views.loadfm),
    path('lo',views.log),
    path("me",views.Med,name='me'),
    path("addme",views.loadme),
    path("base",views.base),
    path("home/",views.home,name='home'),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name='contact'),
    path("hp",views.log),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
