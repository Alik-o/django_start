from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return super().get_queryset().filter(publication_attribute=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.count_views += 1
        obj.save()
        return obj


class BlogCreateView(CreateView):
    fields = ('title', 'content', 'preview', 'publication_attribute')
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog/blog_form.html'


class BlogUpdateView(UpdateView):
    fields = ('title', 'content', 'preview', 'publication_attribute')
    model = Blog
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
