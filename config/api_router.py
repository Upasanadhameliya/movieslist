from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from movieslist.users.api.views import UserViewSet
from movieslist.movies.api.views import MovieViewSet, ActorViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("movies", MovieViewSet)
router.register("actors", ActorViewSet)


app_name = "api"
# user_list = UserViewSet.as_view({'get': 'list'})
# user_detail = UserViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    # path('forgot-password/', ForgotPasswordFormView.as_view()),
] 

urlpatterns += router.urls
