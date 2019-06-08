from django.db import models;
from django.contrib.auth.models import User;
# Create your models here.
Languages=[("js","Java Script"),("py","Python"),
("java","Java"),("html","Hml"),('css',"Css"),('ruby','Ruby'),('php','Php'),('go','Go'),('c','C'),('text','Plain Text')]
class Bin(models.Model):
    title=models.CharField(max_length=100);
    language=models.CharField(max_length=100,
    choices=Languages,default="py");
    author=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name="bins",editable=False);
    content=models.TextField();
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True);
    public=models.BooleanField(default=True);
    private=models.BooleanField(default=False);
    shared_with=models.ManyToManyField(User,blank=True);

    # __str__ retrun string when object being displayed or printed
    def __str__(self):
        return self.title;
