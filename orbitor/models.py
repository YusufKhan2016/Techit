from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 
from django.urls import reverse
from django.core.validators import URLValidator

# Create your models here.


class pricing_category(models.Model):
    plan=models.CharField(max_length=70,blank=False,null=False)
    def __str__(self):
        return self.plan


    
class category(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    def __str__(self) :
        return self.title

class services(models.Model):
    name= models.ForeignKey(category,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='pics')
    Desc= RichTextUploadingField(blank = True, null=True)

class logoslider(models.Model):
    name=models.CharField(max_length=50)
    img =models.ImageField(upload_to='pics')





# team section 
class socialmediaprofile(models.Model):
    social_media_choices = (
        ('linkedin','linkedin'),
        ('twitter','twitter'),
        ('facebook','facebook'),
        ('instagram','instagram'),
        ('pinterest','pinterest'),
        ('youtube','youtube'),
    )

    team_member= models.ForeignKey('team',on_delete=models.CASCADE, related_name='social_media_profiles')
    platform = models.CharField(max_length=20,choices=social_media_choices)
    link = models.URLField(
        validators=[URLValidator(message="Enter a valid URL.")]
    )

    def __str__(self):
        return f"{self.team_member.name}'s {self.platform} Profile"

class team(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    def __str__(self) :
        return self.name


class projectdetail(models.Model):
    title=models.CharField(max_length=100)
    desc=RichTextUploadingField(blank = True, null=True)
    category=models.ForeignKey(category, on_delete=models.CASCADE)
    client =models.CharField(max_length=100)
    startdate=models.DateTimeField(auto_now=False,auto_now_add=False )
    enddate=models.DateTimeField(auto_now=False,auto_now_add=False )
    img = models.ImageField(upload_to='pics')
    url = models.URLField(
        validators=[URLValidator(message="Enter a valid URL.")]
    )
  


class locationdetail(models.Model):
    location_name= models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)

class contactform(models.Model):
    help_category=models.CharField(max_length=200)
    pcategory =models.CharField(max_length=100,blank=True,null=True)
    subject = models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(blank = True, null=True)
    def __str__(self):
        return self.email
    
class blog(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    head0 = models.CharField(max_length=107,default="")
    head1 = RichTextUploadingField(blank = False, null=False,max_length=1000000)
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='pics/blogs',default="")

    def get_absolute_url(self):
        return reverse('blog-single', kwargs={
            'id':self.id
        })
        
class policy(models.Model):
    desc=RichTextUploadingField(blank=False,null=False)


class condition(models.Model):
    terms_condition = RichTextUploadingField(blank=False,null=False)
class faq(models.Model):
    quest=RichTextUploadingField(blank=False,null=False)
    ans=RichTextUploadingField(blank=False,null=False)

class lg(models.Model):
    title=models.CharField()