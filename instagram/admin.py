from django.contrib import admin
from .models import Post

# 방법1
# admin.site.register(Post)

#방법2
# class PostAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Post,PostAdmin)


#방법3
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =['pk','message','created_at','updated_at','is_public']
    list_display_links = ['message']
    # search_fields =['message']
    list_filter = ['created_at']

    # def message_length(self,post):
    #     return len(post.message)