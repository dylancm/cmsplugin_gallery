import threading

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from inline_ordering.models import Orderable

import utils

localdata = threading.local()
localdata.TEMPLATE_CHOICES = utils.autodiscover_templates()
TEMPLATE_CHOICES = localdata.TEMPLATE_CHOICES


class GalleryPlugin(CMSPlugin):

    def copy_relations(self, oldinstance):
        self.image_set = oldinstance.image_set.all()

    template = models.CharField(max_length=255,
                                choices=TEMPLATE_CHOICES,
                                default='cmsplugin_gallery/gallery.html',
                                editable=len(TEMPLATE_CHOICES) > 1)

    def __unicode__(self):
        return _(u'%(count)d image(s) in gallery') % {'count': self.image_set.count()}


class Image(Orderable):

    def get_media_path(self, filename):
        pages = self.gallery.placeholder.page_set.all()
        return pages[0].get_media_path(filename)

    gallery = models.ForeignKey(GalleryPlugin, verbose_name=_("Gallery"))
    src = models.ImageField(_("Image file"), upload_to=get_media_path,
                            height_field='src_height',
                            width_field='src_width')
    src_height = models.PositiveSmallIntegerField(_("Image height"), editable=False, null=True)
    src_width = models.PositiveSmallIntegerField(_("Image height"), editable=False, null=True)
    title = models.CharField(_("Title"), max_length=255, blank=True)
    alt = models.TextField(_("Alt text"), blank=True)

    def __unicode__(self):
        return self.title or self.alt or str(self.pk)


class Youtube(Orderable):

    gallery = models.ForeignKey(GalleryPlugin, verbose_name=_("Gallery"))
    src = models.CharField(_("Youtube URL"), max_length=255)
    title = models.CharField(_("Title"), max_length=255, blank=True)

    def __unicode__(self):
        return self.title or self.src
