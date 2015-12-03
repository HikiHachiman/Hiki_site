from django.shortcuts import render, get_object_or_404
from Hiki.models import Article, Tag, Classification
from django.views.generic.dates import ArchiveIndexView


# Create your views here.


def blog_index(request):
	blogs = Article.objects.all().order_by('pub_date')
	return render(request, 'Hiki/blog_index.html',{"blogs":blogs})