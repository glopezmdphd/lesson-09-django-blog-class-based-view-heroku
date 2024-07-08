
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', RedirectView.as_view(url='blogging/')),  # Redirect root URL to 'blogging/'
    path('polling/', include('polling.urls')),
    path('blogging/', include('blogging.urls')),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),

]
