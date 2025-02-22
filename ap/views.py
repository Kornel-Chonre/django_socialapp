from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm


# Create your views here.
def home(request): #home page display all posts
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/home.html', {'posts': posts})

@login_required
def create_post(request): #create a new post (login-requred)
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


#display loggedin user posts profile page (login-requred)
@login_required
def profile(request):
    user_post = Post.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'posts/profile.html', {'posts': user_post})

#edit post (login requred)
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post update successfully!')
            return redirect('profile')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form})

#delete post (loging-requred)
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method =='POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('profile')
    return render(request, 'posts/delete_post.html', {'post': post})