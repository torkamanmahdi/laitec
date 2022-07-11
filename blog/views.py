from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def create_post(request):
    from .models import Post
    from django.contrib.auth.models import User
    from random import randrange as rd
    me = User.objects.get(username='admin')
    for i in range(50):
        x = rd(100000)
        Post.objects.create(author=me, title=f'Sample title {i}', text=f'Test {i} {x}')
    return HttpResponse('done!')