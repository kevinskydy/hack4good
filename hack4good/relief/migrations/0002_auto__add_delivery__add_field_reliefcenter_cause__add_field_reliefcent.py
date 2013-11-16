# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Delivery'
        db.create_table(u'relief_delivery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relief.Item'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('arrival_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'relief', ['Delivery'])

        # Adding field 'ReliefCenter.cause'
        db.add_column(u'relief_reliefcenter', 'cause',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['relief.Cause']),
                      keep_default=False)

        # Adding field 'ReliefCenter.name'
        db.add_column(u'relief_reliefcenter', 'name',
                      self.gf('django.db.models.fields.CharField')(default='ReliefCenter Name', max_length=64),
                      keep_default=False)

        # Adding field 'ReliefCenter.longitude'
        db.add_column(u'relief_reliefcenter', 'longitude',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ReliefCenter.latitude'
        db.add_column(u'relief_reliefcenter', 'latitude',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Goal.relief_center'
        db.add_column(u'relief_goal', 'relief_center',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['relief.ReliefCenter']),
                      keep_default=False)

        # Adding field 'Goal.target_date'
        db.add_column(u'relief_goal', 'target_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 11, 16, 0, 0)),
                      keep_default=False)

        # Adding field 'Cause.name'
        db.add_column(u'relief_cause', 'name',
                      self.gf('django.db.models.fields.CharField')(default='Cause Name', max_length=128),
                      keep_default=False)

        # Adding field 'Cause.created'
        db.add_column(u'relief_cause', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 16, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'ItemType.name'
        db.add_column(u'relief_itemtype', 'name',
                      self.gf('django.db.models.fields.CharField')(default='ItemType Name', max_length=32),
                      keep_default=False)

        # Adding field 'Item.goal'
        db.add_column(u'relief_item', 'goal',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['relief.Goal']),
                      keep_default=False)

        # Adding field 'Item.item_type'
        db.add_column(u'relief_item', 'item_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['relief.ItemType']),
                      keep_default=False)

        # Adding field 'Item.quota'
        db.add_column(u'relief_item', 'quota',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Delivery'
        db.delete_table(u'relief_delivery')

        # Deleting field 'ReliefCenter.cause'
        db.delete_column(u'relief_reliefcenter', 'cause_id')

        # Deleting field 'ReliefCenter.name'
        db.delete_column(u'relief_reliefcenter', 'name')

        # Deleting field 'ReliefCenter.longitude'
        db.delete_column(u'relief_reliefcenter', 'longitude')

        # Deleting field 'ReliefCenter.latitude'
        db.delete_column(u'relief_reliefcenter', 'latitude')

        # Deleting field 'Goal.relief_center'
        db.delete_column(u'relief_goal', 'relief_center_id')

        # Deleting field 'Goal.target_date'
        db.delete_column(u'relief_goal', 'target_date')

        # Deleting field 'Cause.name'
        db.delete_column(u'relief_cause', 'name')

        # Deleting field 'Cause.created'
        db.delete_column(u'relief_cause', 'created')

        # Deleting field 'ItemType.name'
        db.delete_column(u'relief_itemtype', 'name')

        # Deleting field 'Item.goal'
        db.delete_column(u'relief_item', 'goal_id')

        # Deleting field 'Item.item_type'
        db.delete_column(u'relief_item', 'item_type_id')

        # Deleting field 'Item.quota'
        db.delete_column(u'relief_item', 'quota')


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
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['relief.Item']"}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'ReliefCenter Name'", 'max_length': '64'})
        }
    }

    complete_apps = ['relief']