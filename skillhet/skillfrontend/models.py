from django.db import models
from tinymce import HTMLField
from django.utils.safestring import mark_safe
from django_resized import ResizedImageField

class Slider(models.Model):
    small_title = models.CharField(max_length=255, null=True)
    title_content = HTMLField(default=None, null=True)
    title = models.CharField(max_length=255, null=True)
    image = ResizedImageField(size=[1600, 900] ,upload_to='slider' , null=True)
    
    # For Image Display In Admin
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 200px; height: 100px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    #Show List Name In Admin
    class Meta:
        verbose_name_plural = "Slider Management"

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_slug = models.SlugField(default=None)
    category_image = models.ImageField(upload_to='category' , default=None)
    
    def image_tag(self):
        if self.category_image:
            return mark_safe('<img src="%s" style="width: 64px; height: 64px;" />' % self.category_image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    class Meta:
        verbose_name_plural = "Category Management"

    def __str__(self):
        return self.category_name

class SocialLink(models.Model):
    facebook = models.CharField(max_length=256,default=None)
    twitter = models.CharField(max_length=256,default=None)
    flickr = models.CharField(max_length=256,default=None)
    linkedin = models.CharField(max_length=256,default=None)

    class Meta:
        verbose_name_plural = "Social Link Management"

    def __str__(self):
        return self.facebook

class SiteAddress(models.Model):
    phone = models.CharField(max_length=256,default=None)
    landline = models.CharField(max_length=256,default=None)
    email = models.CharField(max_length=256,default=None)
    web_link = models.CharField(max_length=256,default=None)
    address = models.TextField(default=None)
    footer_content = models.TextField(default=None)

    class Meta:
        verbose_name_plural = "Address Management"

    def __str__(self):
        return self.email

class CoreValue(models.Model):
    first_title = models.CharField(max_length=255, null=True)
    second_title = models.CharField(max_length=255, null=True)
    content = models.TextField(default=None, null=True)
    small_content1 = models.TextField(default=None, null=True)
    small_content2 = models.TextField(default=None, null=True)
    small_content3 = models.TextField(default=None, null=True)
    image = ResizedImageField(size=[272, 300], upload_to='core_value', null=True)
    
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 272px; height: 300px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    class Meta:
        verbose_name_plural = "Core Value Management"

    def __str__(self):
        return self.first_title

class About(models.Model):
    first_title = models.CharField(max_length=255, null=True)
    second_title = models.CharField(max_length=255, null=True)
    content = HTMLField(default=None, null=True)
    image1 = ResizedImageField(size=[400, 400], upload_to='about', null=True)
    image2 = ResizedImageField(size=[400, 400], upload_to='about', null=True)
    signature = models.ImageField(upload_to='about', null=True)
    
    def image_tag(self):
        if self.image1:
            return mark_safe('<img src="%s" style="width: 200px; height: 200px;" />' % self.image1.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    class Meta:
        verbose_name_plural = "About Us Management"

    def __str__(self):
        return self.first_title

class WhyChooseUs(models.Model):
    title = models.CharField(max_length=256,default=None)
    content = models.TextField(default=None)
    image = models.ImageField(upload_to='why_choose_us', default=None)
    
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 64px; height: 64px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    class Meta:
        verbose_name_plural = "Why Choose Us Management"

    def __str__(self):
        return self.title

class PostDetail(models.Model):
    category = models.ForeignKey('Category',default=None, on_delete=models.CASCADE)
    main_content = HTMLField(default=None,null=True)
    slider_image1 = ResizedImageField(size=[1000, 500] ,upload_to='post_details' , default=None, null=True)
    slider_image2 = ResizedImageField(size=[1000, 500] ,upload_to='post_details' , default=None, null=True)
    slider_image3 = ResizedImageField(size=[1000, 500] ,upload_to='post_details' , default=None, null=True)
    
    title1 = models.CharField(max_length=255, null=True)
    content1 = HTMLField(default=None, null=True)
    image1 = ResizedImageField(size=[456, 286] ,upload_to='post_details' , default=None, null=True)

    title2 = models.CharField(max_length=255, null=True)
    content2 = HTMLField(default=None, null=True)
    image2 = ResizedImageField(size=[456, 303] ,upload_to='post_details' , default=None, null=True)
    sub_title1 = models.CharField(max_length=255, null=True)
    sub_title2 = models.CharField(max_length=255, null=True)
    sub_title3 = models.CharField(max_length=255, null=True)

    def image_tag(self):
        if self.slider_image1:
            return mark_safe('<img src="%s" style="width: 200px; height: 100px;" />' % self.slider_image1.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    class Meta:
        verbose_name_plural = "Post Management"

    def __str__(self):
        return self.title1

class OurSkill(models.Model):
    heading = models.CharField(max_length=255, default=None, null=True)

    title1 = models.CharField(max_length=255, default=None, null=True)
    content1 = models.TextField(default=None, null=True)

    title2 = models.CharField(max_length=255, default=None, null=True)
    content2 = models.TextField(default=None, null=True)

    title2 = models.CharField(max_length=255, default=None, null=True)
    content2 = models.TextField(default=None, null=True)

    title3 = models.CharField(max_length=255, default=None, null=True)
    content3 = models.TextField(default=None, null=True)
    image = ResizedImageField(size=[750, 750] ,upload_to='our_skill' , default=None, null=True)

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 200px; height: 200px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    class Meta:
        verbose_name_plural = "Our Skill Management"

    def __str__(self):
        return self.heading

class AdminEmail(models.Model):
    from_email = models.CharField(max_length=256, null=True)
    receive_email = models.CharField(max_length=256, null=True)
    
    class Meta:                        
        verbose_name_plural = "Email Management"

    def __str__(self):
        return self.from_email

class Enquery(models.Model):
    name = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=256, null=True)
    mobile = models.CharField(max_length=256, null=True)
    subject = models.CharField(max_length=256, null=True)
    message = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Enquery Management"

    def __str__(self):
        return self.name

