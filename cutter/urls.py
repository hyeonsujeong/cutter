from django.contrib import admin
from django.urls import path
import post.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', post.views.info, name="info"),
    path('', post.views.index, name='index'), 
    path('csv/', post.views.csv, name="csv"),
    path('conner/', post.views.conner, name="conner"),
    path('embellishment/', post.views.embellishment, name="embellishment"),
    path('manbox/', post.views.manbox, name="manbox"),
    path('ending/', post.views.ending, name="ending"),
]