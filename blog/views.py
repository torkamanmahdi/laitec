from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def create_post(request):
    from django.contrib.auth.models import User
    from random import randrange as rd
    me = User.objects.get(username='admin')
    for i in range(50):
        x = timezone.now()
        a = Post.objects.create(author=me, title=f'Sample title {i} {x}', text=f'Test {i} {x}')
        a.publish()
    return HttpResponse('done!')