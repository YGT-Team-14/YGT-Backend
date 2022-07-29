from django.shortcuts import redirect, render, get_object_or_404
from .forms import Mento_PostModelForm, Friend_PostModelForm
from .models import Mento_Post, Friend_Post


def home(request):
    return render(request,'home.html')

def mento_createpost(request):
    if (request.method == 'POST' or request.method == 'FILES'):
        form = Mento_PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
            return redirect('mentocategory')
    else:
        form = Mento_PostModelForm()
        return render(request, 'mento_create.html',{'form':form})

def friend_createpost(request):
    if (request.method == 'POST' or request.method == 'FILES'):
        form = Friend_PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
            return redirect('friendcategory')
    else:
        form = Friend_PostModelForm()
        return render(request, 'friend_create.html',{'form':form})

def mento_category(request):
    posts = Mento_Post.objects.all()
    return render(request, 'mento_category.html',{'posts':posts})

def friend_category(request):
    posts = Friend_Post.objects.all()
    return render(request, 'friend_category.html',{'posts':posts})

def mento_detail(request, post_id):
    post_detail = get_object_or_404(Mento_Post, pk=post_id)
    return render(request, 'mento_detail.html', {'post_detail':post_detail})

def friend_detail(request, post_id):
    post_detail = get_object_or_404(Friend_Post, pk=post_id)
    return render(request, 'friend_detail.html', {'post_detail':post_detail})

def mento_update(request, post_id):
    post = Mento_Post.objects.get(id=post_id)
    if request.method == 'POST' or request.method == 'FILES':
        update_form = Mento_PostModelForm(request.POST, request.FILES, instance=post)
        if update_form.is_valid():
            update_form.title = request.POST['title']
            update_form.post = request.POST['post']
            update_form.save()
            return redirect('/mento_detail/'+str(post.id),{'post':post})
    else:
        update_form = Mento_PostModelForm(request.POST, instance=post)
        return render(request, 'mento_update.html', {'update_form':update_form})

def friend_update(request, post_id):
    post = Friend_Post.objects.get(id=post_id)
    if request.method == 'POST' or request.method == 'FILES':
        update_form = Friend_PostModelForm(request.POST, request.FILES, instance=post)
        if update_form.is_valid():
            update_form.title = request.POST['title']
            update_form.post = request.POST['post']
            update_form.save()
            return redirect('/friend_detail/'+str(post.id),{'post':post})
    else:
        update_form = Friend_PostModelForm(request.POST, instance=post)
        return render(request, 'friend_update.html', {'update_form':update_form})

def mento_delete(request, post_id):
    post = Mento_Post.objects.get(id=post_id)
    post.delete()
    return redirect('/')

def friend_delete(request, post_id):
    post = Friend_Post.objects.get(id=post_id)
    post.delete()
    return redirect('/')
