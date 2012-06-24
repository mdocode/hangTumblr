from django.db import models

class Blog(models.Model):
    url_name = models.CharField(max_length=200, unique=True)
    updated = models.DateField(auto_now=True)
    def __unicode__(self):
        return self. url_name;

    def url():
        return url_name+'.tumblr.com'


class Post(models.Model):
    blog = models.ForeignKey(Blog)
    id_num = models.CharField(max_length=100, unique=True)
    imgUrl = models.CharField(max_length=200)
    def __unicode__(self):
        return self.id_num

class Tag(models.Model):
    post = models.ForeignKey(Post)
    text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.text



