from django.contrib import admin
from django.utils.html import strip_tags

from .models import *



# Register your models here.

admin.site.register(logo)
class service(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(services,service)

class logo(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(logoslider,logo)



# team section

class profile(admin.ModelAdmin):
    search_fields=('team_member',)
    list_per_page = 20
    list_filter = ('team_member','platform')
    
admin.site.register(socialmediaprofile,profile)

class member(admin.ModelAdmin):
    list_display = ('name', 'rank')


admin.site.register(team, member)

# team section ends


class porfolio(admin.ModelAdmin):
    list_display = ('title', 'client')

admin.site.register(projectdetail,porfolio)

class categories(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(category,categories)
class location(admin.ModelAdmin):
    list_display = ('location_name',)
admin.site.register(locationdetail,location)

class contact(admin.ModelAdmin):
    search_fields=('email','name')
    list_display = ('email','name')
    list_per_page = 10
    
admin.site.register(contactform,contact)

class blogpost(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title','pub_date')
    list_filter = ('category','pub_date')
    list_per_page = 20 
admin.site.register(blog, blogpost)



admin.site.register(policy)

admin.site.register(condition)
class questions(admin.ModelAdmin):
    list_display=('questions',)
    def questions(self, obj):
        return strip_tags(obj.quest)

admin.site.register(faq,questions)
