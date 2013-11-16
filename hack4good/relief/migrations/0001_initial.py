# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cause'
        db.create_table(u'relief_cause', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'relief', ['Cause'])

        # Adding model 'ReliefCenter'
        db.create_table(u'relief_reliefcenter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'relief', ['ReliefCenter'])

        # Adding model 'Goal'
        db.create_table(u'relief_goal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'relief', ['Goal'])

        # Adding model 'Item'
        db.create_table(u'relief_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'relief', ['Item'])

        # Adding model 'ItemType'
        db.create_table(u'relief_itemtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'relief', ['ItemType'])


    def backwards(self, orm):
        # Deleting model 'Cause'
        db.delete_table(u'relief_cause')

        # Deleting model 'ReliefCenter'
        db.delete_table(u'relief_reliefcenter')

        # Deleting model 'Goal'
        db.delete_table(u'relief_goal')

        # Deleting model 'Item'
        db.delete_table(u'relief_item')

        # Deleting model 'ItemType'
        db.delete_table(u'relief_itemtype')


    models = {
        u'relief.cause': {
            'Meta': {'object_name': 'Cause'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'relief.goal': {
            'Meta': {'object_name': 'Goal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'relief.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'relief.itemtype': {
            'Meta': {'object_name': 'ItemType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'relief.reliefcenter': {
            'Meta': {'object_name': 'ReliefCenter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['relief']