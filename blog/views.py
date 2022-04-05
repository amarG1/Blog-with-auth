from re import template
from aiohttp import request
from django.shortcuts import render,redirect
from django.views import generic
from .models import Post
#pagination
from django.core.paginator import Paginator


from django.views.generic.edit import CreateView, DeleteView

from django.contrib import messages


from django.http import HttpResponse
from django.views import View
 
class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')

#creatin g post
class Create(CreateView):
 
    # specify the model for create view
    model = Post
 
    # specify the fields to be displayed
 
    fields = ['title', 'img','slug','author','content',]
    template_name = 'createblog.html'
    
    success_url ="/"
    



#updating Post
from django.views.generic.edit import UpdateView
 
# Relative import of GeeksModel
 
class UpdateView(UpdateView):
    # specify the model you want to use
    template_name = 'createblog.html'
    model = Post
 
    # specify the fields
    fields = ['title', 'img','slug','author','content',]
 
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/"

#deleting Post
class DeleteView(DeleteView):
    # specify the model you want to use
    model = Post
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="/"
    template_name ='confirm_delete.html'

def index(request):
    if request.user.is_anonymous:
        return redirect("/login/")

    
    
        
    return render(request, 'home.html')        

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 3

    
    # queryset = Post.objects.filter(status=1)
    # # set up pagination
    # p = Paginator(Post.objects.filter(status=1), 2)
    # page = request.GET.get('page')
    # venues = p.get_page(page)
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(title__icontains=query)
           
        return qs

    template_name = 'index.html'


    # {'venues':venues }


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
