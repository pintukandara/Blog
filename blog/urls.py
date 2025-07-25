from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.starting_page, name="home-page"),
    path("posts/", views.posts ,name="posts-page" ),
    path("posts/<slug:slug>", views.post_detail, name = "post-detail-page")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
