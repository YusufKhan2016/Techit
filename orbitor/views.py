from django.db.models import Count, Q
from django.core.paginator import  Paginator,EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.mail import send_mail

logos=lg.objects.first()

def get_category_count():
    queryset = blog.objects\
        .values('category__title')\
        .annotate(category_count=Count('category'))\
        .filter(category_count__gt=0)\
        .order_by('category__title')
    return queryset



# Create your views here.
def index(request):
    
    faqs=faq.objects.all()
    imgslider = logoslider.objects.all()
    return render(request, 'index.html', {'imgslider':imgslider,
                                          'faqs':faqs,
                                          'logos':logos,
                                          } )

def about(request):    
    smp=socialmediaprofile.objects.all()
    imgslider = logoslider.objects.all()

    group = team.objects.all()
    return render(request, 'about.html', {'imgslider':imgslider,
                                          'group':group,
                                          'logos':logos,
                                          'smp':smp})

#blog section starts

def blogsidebar(request):
    category_count = get_category_count()
    most_recent = blog.objects.order_by('-pub_date')[:3]
    blogs = blog.objects.all()
    paginator = Paginator(blogs,5)
    page_request_var = 'page'
    page= request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    return render(request, 'blog-sidebar.html',{'queryset':paginated_queryset, 
                                                'page_request_var':page_request_var,
                                                'most_recent':most_recent,
                                                'category_count':category_count,
                                                'logos':logos,
                                                })

def blogsingle(request, id):

    post = get_object_or_404(blog, pk=id )
    first = blog.objects.first()
    last = blog.objects.last()    
    return render(request, 'blog-single.html',{'post':post,'first':first,
                                               'last':last,
                                               'logos':logos,
                                               })

#blog section ends 

def projectdetails(request, id):
        
    projectdetails=get_object_or_404(projectdetail, pk=id)
    return render (request, 'project-details.html',{'projectdetails':projectdetails,
                                                    'logos':logos,
                                                    })

def project(request):
    projectdetails = projectdetail.objects.all()
    return render(request, 'project.html', {'projectdetails':projectdetails,
                                            'logos':logos,
                                            })

def service(request):
    desc=services.objects.all()
    return render(request, 'service.html', {'desc':desc,
                                            'logos':logos,
                                            })


def servicedetails(request,id):
    servedetail=get_object_or_404(services,pk=id)

    context={
        'servedetail':servedetail,
        'logos':logos,
    }
    return render(request,'service-details.html',context)


def contact(request):
    if request.method == 'POST':
        contacts=contactform()
        categor = request.POST.get('category')
        p_category=request.POST.get('plan_category')
        subject = request.POST.get('subject')
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contacts.help_category = categor
        contacts.pcategory=p_category
        contacts.subject =subject
        contacts.name = name
        contacts.email = email 
        contacts.message = message

        contacts.save()
        return redirect('/')
    
    
    pricing=pricing_category.objects.all()
    categorys=category.objects.all()      
    location=locationdetail.objects.all()          
    return render(request, 'contact.html',{'location':location,
                                           'categorys':categorys,
                                           'pricing':pricing,
                                           'logos':logos,
                                           })


def getTopic(request, name):
    cat = get_object_or_404(category, title=name)
    post = blog.objects.filter(category=cat.id)
    category_count = get_category_count()
    most_recent = blog.objects.order_by('-pub_date')[:3]
    paginator = Paginator(post,5)
    page_request_var = 'page'
    page= request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    return render(request, 'category.html', {'post':post,
                                             'queryset':paginated_queryset, 
                                            'page_request_var':page_request_var,
                                            'most_recent':most_recent,
                                            'category_count':category_count,
                                            'logos':logos,
                                            })

def search(request):
    queryset = blog.objects.all()
    query = request.GET.get('q')
    most_recent = blog.objects.order_by('-pub_date')[:3]
    
    if query:
        queryset=queryset.filter(
            Q(title__icontains=query)|
            Q(head0__icontains=query)
        ).distinct()

        context={
            'queryset':queryset,
            'most_recent':most_recent,   
            'logos':logos,         
        }
    return render( request, 'search_results.html', context)




def terms_condition(request):
    protocol=condition.objects.first()

    context={
            'protocol':protocol,
            'logos':logos,

    }
    return render(request,'terms-condition.html',context)


def privacy_policy(request):
    description= policy.objects.first()
    context={
        'description':description,
        'logos':logos,
    }
    return render(request,'privacy-policy.html',context)


