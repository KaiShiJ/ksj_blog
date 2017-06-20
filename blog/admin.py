from django.contrib import admin

# Register your models here.
from models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','create_time','modify_time',)
    list_filter = ('create_time',)

admin.site.register(Article,ArticleAdmin)


