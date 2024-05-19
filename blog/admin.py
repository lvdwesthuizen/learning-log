from django.contrib import admin
from blog.models import Category, Comment, Post

# Register your models here.
#  Their purpose is to customize what the admin pages show - leaving default config for now
class CategoryAdmin(admin.ModelAdmin):
   pass

class PostAdmin(admin.ModelAdmin):
   pass

class CommentAdmin(admin.ModelAdmin):
   pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)