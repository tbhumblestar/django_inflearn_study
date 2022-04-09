from django.db import models

class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False,verbose_name="공개여부")

    def __str__(self):
        return f'customed messages :{self.message}'

    # def message_length(self):
    #     return len(self.message)
    
    # message_length.short_description ="메세지 글자수"
    # created_at.short_description="집에갈래.."
