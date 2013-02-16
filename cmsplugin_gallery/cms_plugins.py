from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

import admin
import models


class CMSGalleryPlugin(CMSPluginBase):

    model = models.GalleryPlugin
    inlines = [admin.ImageInline, admin.YoutubeInline, ]
    name = _('Image gallery')
    render_template = 'cmsplugin_gallery/gallery.html'

    def render(self, context, instance, placeholder):

        videos = instance.youtube_set.all()
        for vid in videos:
            url = vid.src
            split_url = url.split('/')
            vid_id = split_url[-1]
            if (vid_id == '' and len(split_url) > 2):
                vid_id = split_url[-2]
            elif ('v=' in vid_id):
                vid_id = vid_id.split('=')[-1]
            vid.thumb_url = "http://img.youtube.com/vi/%s/2.jpg" % (vid_id, )

        context.update({
                        'images': instance.image_set.all(),
                        'videos': videos,
                        'gallery': instance,
                       })
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(CMSGalleryPlugin)
