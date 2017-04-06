from django.contrib import admin
from django.utils.timezone import now
from esiomotores.blog.models import Blogs, Contents


# Esta classe permitirá que a tabela CONTENTS seja mostrada dentro do registro do BLOG
class ContentInLine(admin.TabularInline):
    model = Contents
    extra = 0 # Seta quantas linhas Content serão inicialmente mostradas no registro do Blog
    list_display = ['order_out']

class BlogsModelAdmin(admin.ModelAdmin):
    inlines = [ContentInLine] # Faz referência à classe criada acima
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'publish', 'slug']
    list_display = ['title', 'publish', 'category', 'slug', 'sent_today']
    list_filter = ('category','publish')
    ordering = ('-created_at',)

    def sent_today(self, obj):
        return obj.created_at.date() == now().date()

    sent_today.short_description = 'enviada hoje?'
    sent_today.boolean = 'True'


admin.site.register(Blogs, BlogsModelAdmin)
