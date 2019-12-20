from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import SignUpView
from news.views import NewsList
# from django.conf import settings
# from django.conf.urls.static import static
urlpatterns = [
    
    path('signup/success/', views.success, name='success'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),

   
]


