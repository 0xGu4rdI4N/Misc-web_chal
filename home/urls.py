from django.contrib import admin
from django.urls import path,include
from home import views
from itertools import product
# import views

l=[]
for i in product('abcdefghjklmnpqrtuvwyz',repeat=4):
    l.append(i)



urlpatterns = [
    path('',views.index,name='home'),
    path('robots.txt',views.robots)
]
for j in l:
    i=''.join(j)
    code=f"path('{i}',views.{i})"
    code=eval(code)
    urlpatterns.append(code)
