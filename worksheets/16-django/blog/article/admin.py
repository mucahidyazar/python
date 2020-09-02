from django.contrib import admin
from .models import Article

# Register your models here.

#admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
  list_display = ['title', 'author','created_data', 'content']
  list_display_links = ['title', 'created_data']
  search_fields = ['title', 'content']
  list_filter = ['created_data']
  class Meta:
    model = Article