"""rare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include
from rest_framework import routers
from rareapi.views import register_user, login_user, CategoryViewSet, CommentViewSet, TagViewSet, SubscriptionViewSet, UserViewSet, RareUserViewSet, ImageViewSet
from rareapi.views.post import PostViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet, 'category')
router.register(r'comments', CommentViewSet, 'comment')
router.register(r'posts', PostViewSet, 'post')
router.register(r'tags', TagViewSet, 'tag')
router.register(r'rareusers', RareUserViewSet, 'rareuser')
router.register(r'subscriptions', SubscriptionViewSet, 'subscription')
router.register(r'users', UserViewSet, 'user' )
router.register(r'images', ImageViewSet, 'image')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
