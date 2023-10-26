from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
class PostListView(ListView):
    model = Post
    template_name = 'post.html'
class FullPostView(DetailView):
    model = Post
    template_name = 'full_post.html'
class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title','photo','body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class UpdatePostView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post 
    template_name = 'edit_post.html'
    fields = ['title','photo','body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user