from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import  AdminEmail, Slider, Category, SocialLink, SiteAddress, About, WhyChooseUs, Enquery, CoreValue, PostDetail, OurSkill
admin.site.unregister(User)
admin.site.unregister(Group)

class AdminEmailAdmin(admin.ModelAdmin):
    list_display = ('from_email','receive_email') 
    def has_add_permission(self, request, obj=None):  
        return False

class SliderAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag') #Display Image & Title
    def has_add_permission(self, request, obj=None):  #For Stop Add Button
        return False

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"category_slug": ("category_name",)}
    list_display = ('category_name', 'image_tag', 'category_slug',)
    def has_add_permission(self, request, obj=None):  
        return False

class SociallinkAdmin(admin.ModelAdmin):
    list_display = ('facebook','twitter','flickr','linkedin')
    def has_add_permission(self, request, obj=None):  
        return False

class SiteAddressAdmin(admin.ModelAdmin):
    list_display = ('phone','landline','email','address')
    def has_add_permission(self, request, obj=None):  
        return False

class AboutAdmin(admin.ModelAdmin):
    list_display = ('first_title','second_title','image_tag')
    def has_add_permission(self, request, obj=None):  
        return False

class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag','content')
    def has_add_permission(self, request, obj=None):  
        return False

class EnqueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'subject', 'message')
    def has_add_permission(self, request, obj=None):  
        return False

class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('first_title', 'second_title', 'content', 'image_tag')
    def has_add_permission(self, request, obj=None):  
        return False

class PostDetailAdmin(admin.ModelAdmin):
    list_display = ('main_content', 'title1', 'title2', 'image_tag')
    def has_add_permission(self, request, obj=None):  
        return False

class OurSkillAdmin(admin.ModelAdmin):
    list_display = ('heading', 'title1', 'content1', 'image_tag')
    def has_add_permission(self, request, obj=None):  
        return False
   

admin.site.register(Slider, SliderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SocialLink, SociallinkAdmin)
admin.site.register(SiteAddress, SiteAddressAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(WhyChooseUs, WhyChooseUsAdmin)
admin.site.register(Enquery, EnqueryAdmin)
admin.site.register(CoreValue, CoreValueAdmin)
admin.site.register(PostDetail, PostDetailAdmin)
admin.site.register(OurSkill, OurSkillAdmin)
admin.site.register(AdminEmail, AdminEmailAdmin)
