import uuid
from cloudinary.models import CloudinaryField
# from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _

from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase


LAN = (
    ('Js','JS'),
    ('Django','DJANGO'),
    ('Flask','FLASK'),
    ('React','REACT'),
    ('Angular','ANGULAR'),
    ('Ruby','RUBY'),
    ('Rails','RAILS'),
)

class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    # tag = models.ForeignKey(Tag, related_name="uuid_tagged_items", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
    

class Code(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, null=True, blank=True)
    picture = CloudinaryField('image')
    description = models.TextField(max_length=1000, null=True, blank=True)
    language = TaggableManager(through=UUIDTaggedItem)
    featured = models.BooleanField(default=False)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('singleproduct', args=[str(self.uuid)])

class Image(models.Model):
    projects = models.ForeignKey(Code, on_delete=models.CASCADE, default=None, blank=True, null=True)
    other_images = CloudinaryField('image')
    video = CloudinaryField(resource_type='video')
    
    def __str__(self):
        return self.projects.title
    