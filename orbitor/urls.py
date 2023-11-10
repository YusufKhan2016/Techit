from django.urls import path
from . import views

urlpatterns =[
    path('/',views.index, name='index'),
    path('about',views.about, name='about'),
    path('blog-sidebar',views.blogsidebar, name='blog-sidebar'),
    path('blog-single/<int:id>',views.blogsingle, name= 'blog-single'),
    path('project-details/<int:id>',views.projectdetails, name='project-details'),
    path('project', views.project, name='project'),
    path('service',views.service, name='service'),
    path('service-details/<int:id>', views.servicedetails, name='service-details'),

    path('contact',views.contact, name='contact'),
    path('topic/<name>', views.getTopic, name='topic'),
    path('search',views.search,name='search'),
  
    path('terms-condition',views.terms_condition, name='terms-condition'),
    path('privacy-policy',views.privacy_policy, name='privacy-policy')

]