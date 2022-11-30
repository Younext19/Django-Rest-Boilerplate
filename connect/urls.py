from django.urls import include, path
from connect.views import UserInfo, SignUp

urlpatterns = [
    path('connect/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('connect/userinfo/', UserInfo.as_view()),
    path('connect/signup/', SignUp.as_view(), name='signup'),

]
