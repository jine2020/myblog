from .models import Category,Banner,Article,Tag,Link
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
#首页
def index(request):
    allcategory=Category.objects.all()
    banner=Banner.objects.filter(is_active=True)[0:4]
    tui=Article.objects.all().order_by('-views')[:3]
    allarticle=Article.objects.all().order_by('-id')[0:2]
    hot=Article.objects.all().order_by('-views')[:10]
    renmen=Article.objects.filter(tui__id=6).order_by('-views')[:5]
    tags=Tag.objects.all()
    link=Link.objects.all()
    context={
        'allcategory':allcategory,
        'banner':banner,
        'tui':tui,
        'allarticle':allarticle,
        'hot':hot,
        'remen':renmen,
        'tags':tags,
        'link':link,
    }
    return render(request,'index.html',context)

#列表页
def list(request,lid):
    list=Article.objects.filter(category__id=lid)
    cname=Category.objects.get(id=lid)
    hot = Article.objects.all().order_by('-views')[:10]
    remen=Article.objects.filter(tui__id=6).order_by('-views')[:5]
    allcategory=Category.objects.all()
    tags=Tag.objects.all()
    page=request.GET.get('page')
    paginator=Paginator(list,5)
    try:
        list=paginator.page(page)
    except PageNotAnInteger:
        list=paginator.page(1)
    except EmptyPage:
        list=paginator.page(paginator.num_pages)
    return render(request,'list.html',locals())

#内容页
def show(request,sid):
    show = Article.objects.get(id=sid)#查询指定ID的文章
    allcategory = Category.objects.all()#导航上的分类
    tags = Tag.objects.all()#右侧所有标签
    hot = Article.objects.all().order_by('-views')[:10]
    remen = Article.objects.filter(tui__id=6).order_by('-views')[:5]#右侧热门推荐
    previous_blog = Article.objects.filter(create_time__gt=show.create_time,category=show.category.id).first()
    netx_blog = Article.objects.filter(create_time__lt=show.create_time,category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'show.html', locals())
#标签页
def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)
    hot = Article.objects.all().order_by('-views')[:10]
    remen = Article.objects.filter(tui__id=6).order_by('-views')[:5]
    allcategory = Category.objects.all()
    tname = Tag.objects.get(name=tag)
    tags = Tag.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'tags.html', locals())

# 搜索页
def search(request):
    ss=request.GET.get('search')
    list=Article.objects.filter(title__icontains=ss)
    hot = Article.objects.all().order_by('-views')[:10]
    remen=Article.objects.filter(tui__id=6).order_by('-views')[:5]
    allcategory=Category.objects.all()
    tags = Tag.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'search.html', locals())
# 关于我们
def about(request):
    allcategory=Category.objects.all()
    return render(request,'page.html',locals())