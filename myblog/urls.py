
from django.contrib import admin
from django.urls import path,include,re_path
from blog import views
from django.views.static import serve
from myblog import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('list-<int:lid>.html',views.list,name='list'),
    path('show-<int:sid>.html',views.show,name='show'),
    path('tag/<tag>',views.tag,name='tags'),
    path('s/',views.search,name='search'),
    path('about/',views.about,name='about'),
    path('ueditor/',include('DjangoUeditor.urls')),
    re_path('^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
