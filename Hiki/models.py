# coding:utf-8
from django.db import models
import datetime
from django.core.urlresolvers import reverse

# Create your models here.

class Tag(models.Model):
	"""Tags reflect to articles, Many to many"""
	tag_name = models.CharField(max_length=20)
	pub_date =models.DateTimeField

	def __unicode__(self):
		return self.tag_name


class Author(models.Model):
	name = models.CharField(max_length=30)
	email =models.EmailField(blank=True)        #可以为空值
	website = models.URLField(blank=True)

	def __unicode__(self):
		return self.name


class Classification(models.Model):
	"""显示在文章首页的内容摘要标签"""         
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return u'%s' % (self.name)


class Article(models.Model):
	url = models.URLField()
	title = models.CharField(max_length=50)
	title_zh = models.CharField(max_length=50)
	author = models.ForeignKey(Author)
	content_md = models.TextField()
	content_html = models.TextField()
	tags = models.ManyToManyField(Tag,blank=True)      #tag作为重要的文章索引
	views = models.IntegerField()
	pub_date = models.DateTimeField('Data published')
	up_date = models.DateTimeField('Data updated')
	classification = models.ForeignKey(Classification)		

	def get_absolute_url(self):
		return reverse('article-detail', kwargs={'pk':self.pk})