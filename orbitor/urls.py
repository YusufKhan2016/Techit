from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('about.html',views.about, name='about'),
    path('blog-sidebar.html',views.blogsidebar, name='blog-sidebar'),
    path('blog-single.html/<int:id>',views.blogsingle, name= 'blog-single'),
    path('project-details.html/<int:id>',views.projectdetails, name='project-details'),
    path('project.html', views.project, name='project'),
    path('service.html',views.service, name='service'),
    path('service-details.html/<int:id>', views.servicedetails, name='service-details'),
    path('index.html',views.index, name='index'),
    path('contact.html',views.contact, name='contact'),
    path('topic/<name>', views.getTopic, name='topic'),
    path('search',views.search,name='search'),
  
    path('terms-condition.html',views.terms_condition, name='terms-condition'),
    path('privacy-policy.html',views.privacy_policy, name='privacy-policy')

]