from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from todolist_app import views as todolist_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_views.index, name='index'),
    path('todolist/', include('todolist_app.urls')),
    path('accounts/', include('users_app.urls')),
    path('contact', todolist_views.contact, name='contact'),
    path('about-us', todolist_views.about, name='about'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

