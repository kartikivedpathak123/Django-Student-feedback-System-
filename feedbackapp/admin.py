from django.contrib import admin
from feedbackapp.models import Feedback
# Register your models here.
#admin.site.register(Product)
class FeedbackAdmin(admin.ModelAdmin):
    list_display=['name','message','email','created_at']
    list_filter=['created_at']

admin.site.register(Feedback,FeedbackAdmin)
