from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'Hiki.views.blog_index', name='blog_index'),

]