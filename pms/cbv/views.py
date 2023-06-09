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