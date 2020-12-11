from django.shortcuts import render
from blog.models import Post,Category,Tag

# Create your views here.

def post_list(request,category_id=None,tag_id=None):
    category = tag = None
    if category_id:
        category,post_list = Post.get_by_category(category_id)
    elif tag_id:
        tag,post_list = Post.get_by_tag(tag_id)
    else:
        post_list = Post.latest_post()

    context={
        'category':category,
        'tag':tag,
        'post_list':post_list,
    }

    return render(request,'blog/blog.html',context)



