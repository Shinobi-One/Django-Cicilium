from django.contrib import admin
from .models import Article ,Category

from django_jalali.admin.filters import JDateFieldListFilter
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display= ('title','slug','status')
    list_filter =  ('published_at'),

    search_fields = ('description',)
    prepopulated_fields = {'slug':('title',)}
    
    
    
    
    
    
class CatgoryAdmin(admin.ModelAdmin):
    list_display = ('title','position')
    search_fields = ('position',)
    prepopulated_fields = {'slug':('title',)}
    
    
admin.site.register(Article , ArticleAdmin),
admin.site.register(Category,CatgoryAdmin)
