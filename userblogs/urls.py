from django.urls import path
from userblogs import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.blogs),
    path('user_readmore/<bid>',views.user_read_more),
    path('user_blog',views.user_blogs),
    path('add_blog',views.add_blog),
    path('update/<bid>',views.update_blog),
    path('delete/<did>',views.delete_blog),
    path('bfilter/<bfilter>',views.blog_filter),
    path('search',views.search),
    path('contact',views.contact),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)