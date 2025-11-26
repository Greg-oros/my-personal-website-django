from django.urls import path
from .views import home_page_view, AboutPageView, ContactView, SuccessView


# fmt: off
urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"), # new
    path("", home_page_view, name="home"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),
]

# fmt: on
