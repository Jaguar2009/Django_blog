from django.shortcuts import render
from Django_blog.blog.models import Post, Comment


def post_list(reguest):
    posts = Post.objects.all()
    context = {
        "posts_list": posts,
    }
    return render(
        reguest,
        "blog_html/post_list.html",
        context=context,
    )


def get_post_by_id(request, post_id):
    post_details = Post.objects.get(id=post_id)
    post_details_comment = Comment.objects.filter(post=post_details)
    context = {
        "post_detail": post_details,
        'post_detail_comment': post_details_comment,
    }
    return render(
        request,
        "blog_html/post_details.html",
        context=context
    )


def search_posts_by_author_name(request):
    query = request.GET.get('author_name', '')
    posts = Post.objects.filter(author__name__icontains=query) if query else Post.objects.none()

    context = {
        'posts': posts,
        'query': query
    }

    return render(request, 'blog_html/posts_by_author.html', context)