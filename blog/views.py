from django.shortcuts import render,redirect
from .models import PostModel
from .forms import PostModelForm,PostUpdateForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator





@login_required
def index(request):
    post_list = PostModel.objects.all()
    paginator = Paginator(post_list, 3) 

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    if request.method == "POST":
        form = PostModelForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("blog-index")
    else:
        form = PostModelForm()

    context = {
        "posts": posts,
        "form": form,
    }

    return render(request, "blog/index.html", context)

@login_required
def post_detail(request,pk):
    post=PostModel.objects.get(id=pk)
    if request.method=="POST":
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            instance=comment_form.save(commit=False)
            instance.user=request.user
            instance.post=post
            instance.save()
            return redirect("blog-detail",pk=post.id)
    else:
        comment_form=CommentForm()
    context={
        "post":post,
        "comment_form":comment_form
    }
    return render(request,'blog/post_detail.html',context)

@login_required
def post_edit(request,pk):
    post=PostModel.objects.get(id=pk)
    if request.method=="POST":
        form=PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog-detail",pk=post.id)
    else:
        form=PostUpdateForm(instance=post)
    context={
        "post":post,
        "form":form
    }
    return render(request,"blog/post_edit.html",context)

@login_required
def post_delete(request,pk):
    post=PostModel.objects.get(id=pk)
    if request.method=="POST":
        post.delete()
        return redirect("blog-index")

    context={
        "post":post
    }
    return render(request,'blog/post_delete.html',context)





