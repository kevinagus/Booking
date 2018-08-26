from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'login$', LoginView.as_view(template_name="client/login_form.html"), name="client_login"),
    url(r'logout$', LogoutView.as_view(), name="client_logout")
]
