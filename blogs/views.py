from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views import generic
from .models import blog
from .forms import CommentForm, BlogForm

def BlogDetailView(request, pk):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.Blog = get_object_or_404(blog, pk=pk)
            context = {
                'form' : form
            }
            form.save()
            print(form)
            return redirect(reverse('detail', kwargs={
                'pk' : pk
            }))
        else:
            form = CommentForm()
    blog_pk = get_object_or_404(blog, pk=pk)
    context = {
        'blog' : blog_pk,
        'form' : form
    }

    print(blog_pk.Comment)
    return render(request, 'blog/blog-detail.html', context)


class BlogListView(generic.ListView):
    model = blog
    context_object_name = 'blog_set'
    template_name = 'blog/list.html'

def Search(request):
    if 'search' in request.GET:
        q = ''
        if 'search' in request.GET:
            print("p")

            q = request.GET['search']
            blog_set = blog.objects.all().filter(title__icontains=q).distinct()

            context = {
                'blog_set' : blog_set
            }

            return render(request, 'blog/list.html', context)
    form = CommentForm()


class BlogAdd(generic.FormView):
    template_name = 'blog/blog-form.html'
    form_class = BlogForm
    success_url = reverse_lazy('list')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



def BlogUpdate(request, pk):
    instance = get_object_or_404(blog, pk=pk)
    form = BlogForm(request.POST or None, instance=instance)
    print("p")
    print(form)
    if form.is_valid():
        print("p")

        form.save()
        print(form)
        return redirect(reverse('list'))
    print("p")

    return render(request, 'blog/blog-form.html', {'form': form})


def BlogDelete(request):
    pass