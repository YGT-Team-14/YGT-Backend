"""YGT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from postapp import views
from users import views as userview


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login', userview.login, name='login'),
    path('signup', userview.signup, name='signup'),

    path('', views.intro, name='intro'),
    path('home', views.home, name='home'),

    path('mentocreatepost', views.mento_createpost, name='mentocreatepost'),
    path('friendcreatepost', views.friend_createpost, name='friendcreatepost'),

    path('mentocategory', views.mento_category, name='mentocategory'),
    path('friendcategory', views.friend_category, name='friendcategory'),
    
    path('mento_detail/<int:post_id>', views.mento_detail, name='mentodetail'),
    path('friend_detail/<int:post_id>', views.friend_detail, name='frienddetail'),

    path('detail/<int:post_id>/mentoupdate',views.mento_update, name="mentoupdate"),
    path('detail/<int:post_id>/mentodelete',views.mento_delete, name="mentodelete"),
    path('detail/<int:post_id>/friendupdate',views.friend_update, name="friendupdate"),
    path('detail/<int:post_id>/frienddelete',views.friend_delete, name="frienddelete"),

    #댓글 작성
    path('new_mentocomment/<int:post_id>', views.new_mentocomment, name='new_mentocomment'),

    #좋아요
    path('mentopost_like/<int:post_id>', views.mentopost_like, name='mentopost_like'),
]
