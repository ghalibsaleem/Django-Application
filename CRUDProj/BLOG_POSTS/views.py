from django.shortcuts import get_object_or_404, redirect, render
from .models import PostModel
from .forms import PostDetailsForm

# Create your views here.
def post_list(request):
    posts = PostModel.objects.all()
    return render(request, 'BLOG_POSTS/Index.html', {'post_list':posts})


def post_create(request):
    s_form = PostDetailsForm(request.POST or None)
    print(s_form)
    if s_form.is_valid():
        s_form.save()
        return redirect('BPOST')
    return render(request, 'BLOG_POSTS/post_update.html', {'form_post': s_form})

def post_view(request,pk):
    t_post = get_object_or_404(PostModel,pk=pk)
    return render(request, 'BLOG_POSTS/details.html', {'t_post':t_post})


def post_update(request,pk):
    t_post = get_object_or_404(PostModel,pk=pk)
    t_form = PostDetailsForm(request.POST or None, instance=t_post)
    
    if t_form.is_valid():
        t_form.save()
        return redirect('BPOST')
    return render(request, 'BLOG_POSTS/post_update.html', {'form_post':t_form})

def post_delete(request,pk):
    t_post = get_object_or_404(PostModel,pk=pk)

    if request.method == 'POST':
        t_post.delete()
        return redirect('BPOST')
    return render(request, 'BLOG_POSTS/post_delete.html', {'t_post':t_post})
    