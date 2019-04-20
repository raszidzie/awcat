from django.contrib import admin
from .models import Contact, Post,Comment

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    
    

    list_display = ['email',]

    class Meta:
        model = Contact
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)} 

    class Meta:
        model = Post

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post',]


    class Meta:
        model = Comment

admin.site.register(Post,PostAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Comment,CommentAdmin)
