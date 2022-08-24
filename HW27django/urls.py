from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ads.views import service, categories, ads, users

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", service.index),

    path("cat/", categories.CategoryListView.as_view()),
    path("cat/create/", categories.CategoryCreateView.as_view()),
    path("cat/<int:pk>/", categories.CategoryDetailView.as_view()),
    path('cat/<int:pk>/update/', categories.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', categories.CategoryDeleteView.as_view()),

    path("ad/", ads.AdListView.as_view()),
    path("ad/create/", ads.AdCreateView.as_view()),
    path('ad/<int:pk>/update/', ads.AdUpdateView.as_view()),
    path('ad/<int:pk>/', ads.AdDetailView.as_view()),
    path('ad/<int:pk>/delete/', ads.AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', ads.AdImageView.as_view()),

    path('user/', users.UserListView.as_view()),
    path('user/<int:pk>/', users.UserDetailView.as_view()),
    path("user/create/", users.UserCreateView.as_view()),
    path('user/<int:pk>/update/', users.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', users.UserDeleteView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
