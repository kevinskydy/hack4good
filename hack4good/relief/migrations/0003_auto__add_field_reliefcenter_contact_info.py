# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ReliefCenter.contact_info'
        db.add_column(u'relief_reliefcenter', 'contact_info',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ReliefCenter.contact_info'
        db.delete_column(u'relief_reliefcenter', 'contact_info')


    models = {
        u'relief.cause': {
            'Meta': {'object_name': 'Cause'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 16, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Cause Name'", 'max_length': '128'})
        },
        u'relief.delivery': {
            'Meta': {'object_name': 'Delivery'},
            'arrival_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deliveries'", 'to': u"orm['relief.Item']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        u'relief.goal': {
            'Meta': {'object_name': 'Goal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relief_center': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['relief.ReliefCenter']"}),
            'target_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 16, 0, 0)'})
        },
        u'relief.item': {
            'Meta': {'object_name': 'Item'},
            'goal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['relief.Goal']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['relief.ItemType']"}),
            'quota': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'relief.itemtype': {
            'Meta': {'object_name': 'ItemType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'ItemType Name'", 'max_length': '32'})
        },
        u'relief.reliefcenter': {
            'Meta': {'object_name': 'ReliefCenter'},
            'cause': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['relief.Cause']"}),
            'contact_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'ReliefCenter Name'", 'max_length': '64'})
        }
    }

    complete_apps = ['relief']