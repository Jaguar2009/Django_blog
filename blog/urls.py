from django.urls import path
import Django_blog.blog.views as blog_views

urlpatterns = [
    path('', blog_views.post_list, name="post_list"),
    path('<int:post_id>/', blog_views.get_post_by_id, name='post_details'),
    path('search/', blog_views.search_posts_by_author_name, name='search_posts_by_author_name'),
]