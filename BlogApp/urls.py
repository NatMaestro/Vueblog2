
from django.contrib import admin
from django.urls import path, include, re_path
from users.forms import UserForm
from django_registration.backends.one_step.views import RegistrationView
from main.views import Index
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/register/', RegistrationView.as_view(
                 form_class = UserForm, 
         success_url = "/", 
    ), 
    name=  'register'),

    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('accounts/', include("django.contrib.auth.urls")),



    path('api/', include("users.urls")),
    path('api/', include("articles.urls")),
    path('auth/', include("rest_framework.urls")),
    path('rest-auth/', include("dj_rest_auth.urls")),
    path('rest-auth/registration/', include("dj_rest_auth.registration.urls")),
    path('', Index.as_view(), name="index"), 
        # Catch-all pattern that serves the frontend (Vue app) for any other route
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),

]
