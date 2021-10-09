from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Posting


from django.http import HttpResponseRedirect

from django.contrib import messages


class PostList(ListView):
    model = Posting
    template_name_suffix = '_list'



class PostCreate(CreateView):
    model = Posting
    fields = ['posting_author', 'posting_title', 'posting_text']
    template_name_suffix = '_create'
    #success_url = '/'

    def form_valid(self, form):
        form.instance.posting_author_id = self.request.user.id
        if form.is_valid():
            # 올바르다면
            form.instance.save()
            return redirect('/')
        else:
            # 올바르지 않다면
            return self.render_to_response({'form': form})


class PostUpdate(UpdateView):
    model = Posting
    fields = ['posting_author', 'posting_title', 'posting_text']
    template_name_suffix = '_update'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '수정할 권한이 없습니다.')
            return HttpResponseRedirect('/')
        else:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)

class PostDelete(DeleteView):
    model = Posting
    template_name_suffix = '_delete'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '삭제할 권한이 없습니다.')
            return HttpResponseRedirect('/')
        else:
            return super(PostDelete, self).dispatch(request, *args, **kwargs)


class PostDetail(DetailView):
    model = Posting
    template_name_suffix = '_detail'


