from inline_ordering.admin import OrderableTabularInline
import forms
import models


class ImageInline(OrderableTabularInline):

    model = models.Image

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'src':
            kwargs.pop('request', None)
            kwargs['widget'] = forms.AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageInline, self).\
            formfield_for_dbfield(db_field, **kwargs)


class YoutubeInline(OrderableTabularInline):

    model = models.Youtube
