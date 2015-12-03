from django.contrib import admin
from Hiki.models import Tag, Author, Article, Classification
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	"""docstring for AuthorAdmin"""
	list_display = ('name', 'email', 'website')
	search_fields = ('name',)
		

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'classification', 'author', 'pub_date', 'up_date')
	list_filter = ('pub_date',)
	date_hierarchy = 'pub_date'
	ordering = ('-pub_date',)
	filter_horizontal = ('tags',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Classification)
	
