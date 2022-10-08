from django.contrib import admin
from django.urls import path
from posts.views import main, post_detail, create_post, edit_post
from users.views import register, login_, logout_, users, personal_info, set_password
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="post_all_url"),
    path('posts/<int:id>/', post_detail),
    path('posts/create/', create_post),
    path('posts/<int:id>/edit/', edit_post),

    path('users/register/', register),
    path('users/login/', login_),
    path('users/logout/', logout_),

    path('users/<int:user_id>/', users),
    path('personal/', personal_info),
    path('users/<int:id>/change_password/', set_password)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
