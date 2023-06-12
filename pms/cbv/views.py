from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.

class CreatePost(CreateView):
    model = Post
    fields = ['title', 'body', 'date', 'time']
    template_name = 'cbv/createpost.html'
    success_url = '/cbv/list'


class ListAllPost(ListView):
    model = Post
    template_name = 'cbv/listallpost.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'cbv/detail.html'
    context_object_name = 'post'

class PostDelete(DeleteView):
    model = Post
    template_name = 'cbv/delete.html'
    success_url = '/cbv/list'

class PostUpdate(UpdateView):
    model = Post
    template_name = 'cbv/update.html'
    fields = '__all__'
    success_url = '/cbv/list'


