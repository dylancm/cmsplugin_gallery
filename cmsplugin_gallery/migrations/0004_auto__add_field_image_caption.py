# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Image.caption'
        db.add_column('cmsplugin_gallery_image', 'caption',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=1000, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Image.caption'
        db.delete_column('cmsplugin_gallery_image', 'caption')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 13, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_gallery.galleryplugin': {
            'Meta': {'object_name': 'GalleryPlugin', 'db_table': "'cmsplugin_galleryplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'cmsplugin_gallery/gallery.html'", 'max_length': '255'})
        },
        'cmsplugin_gallery.image': {
            'Meta': {'ordering': "('inline_ordering_position',)", 'object_name': 'Image'},
            'alt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'caption': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_gallery.GalleryPlugin']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inline_ordering_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'src': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'src_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'src_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_gallery']