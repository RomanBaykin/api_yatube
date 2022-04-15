from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from .views import PostViewSet, GroupViewSet, CommentViewSet

router_v1 = SimpleRouter()
router_v1.register(r'posts', PostViewSet)
router_v1.register(r'groups', GroupViewSet)
router_v1.register(r'^posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments')
router_v1.register(r'^posts/(?P<post_id>\d+)/comments/(?P<id>\d+)',
                   CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_v1.urls))
]
