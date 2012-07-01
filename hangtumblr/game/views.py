from django.http import HttpResponse
from django.shortcuts import render_to_response
from hangtumblr.game.models import Blog, Post, Tag
import datetime
import hangblogs
import json
import string
from django.core import serializers
from minidetector import detect_mobile

def hello(request, name=""):
    return HttpResponse("Hello world")

@detect_mobile
def game(request, name):
    posts = Post.objects.filter(blog=Blog.objects.get(url_name=name)).order_by('?')[:3]
    imgs = [post.imgUrl for post in posts]
                       
    t = [['#'+string.lower(tag.text) for tag in post.tag_set.all()] for post in posts]

    json_imgs = json.dumps(imgs)
    t0 = json.dumps(t[0])
    t1 = json.dumps(t[1])
    t2 = json.dumps(t[2])

    if request.mobile:
        return render_to_response("hangtumblr_mobile.html", {'baseurl':name, 'images':json_imgs, 't1':t1, 't2':t2, 't0':t0})
    else:
        return render_to_response("hangtumblr.html", {'baseurl':name, 'images':json_imgs, 't1':t1, 't2':t2, 't0':t0})

def grabRandomPostAsJson(request, name):
    post = Post.objects.filter(blog=Blog.objects.get(url_name=name)).order_by('?')[0]
    tagList = ['#'+string.lower(tag.text) for tag in post.tag_set.all()]
   
    postDict = {'baseurl': name, 'images':post.imgUrl, 'tags':tagList}
    #return render_to_response("test.html", {'baseurl': name, 'images':json.dumps(post.imgUrl), 'tags': json.dumps(tagList)})
    return HttpResponse(json.dumps(postDict))
    
def start(request):
    return render_to_response("submit.html")

def found(request):
    if request.method == 'POST':
        name = request.POST['blogName']
        if updatedToday(name):
            return render_to_response("found.html", {'blogUrl':name})
        else:
            if uploadBlog(name):
                return render_to_response("found.html", {'blogUrl':name})
            else:
                return render_to_response("notfound.html", {'blogUrl':name})
    else:
        return HttpResponse("Hello world")

def updatedToday(blogName):
    try:
        blog = Blog.objects.get(url_name=blogName)
        if blog.updated == datetime.date.today():
            return True
        else:
            return False
    except Blog.DoesNotExist:
        return False

def uploadBlog(blogName):
    itBlog = hangblogs.ImageTagBlog(blogName)
    if (itBlog.hangPosts == None):
        return False
    try:
        b = Blog.objects.get(url_name=blogName)
    except Blog.DoesNotExist:
        b = Blog(url_name=blogName)
        b.save()
    for post in itBlog.hangPosts:
        try:
            p = Post.objects.get(id_num=post.id)
        except Post.DoesNotExist:
            p = Post(blog=b, id_num=post.id, imgUrl=post.photo)
            p.save()
            for tag in post.tags:
                t = Tag(post=p, text=tag)
                t.save()
    return True;

    
