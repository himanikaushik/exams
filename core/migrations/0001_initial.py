# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exam'
        db.create_table('core_exam', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('core', ['Exam'])

        # Adding model 'Section'
        db.create_table('core_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('exam', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Exam'])),
            ('instructions', self.gf('django.db.models.fields.TextField')()),
            ('negation', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal('core', ['Section'])

        # Adding model 'Course'
        db.create_table('core_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('core', ['Course'])

        # Adding model 'Question'
        db.create_table('core_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('points', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Course'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Section'])),
        ))
        db.send_create_signal('core', ['Question'])

        # Adding model 'Answer'
        db.create_table('core_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answer', to=orm['core.Question'])),
            ('option', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('explanation', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'Exam'
        db.delete_table('core_exam')

        # Deleting model 'Section'
        db.delete_table('core_section')

        # Deleting model 'Course'
        db.delete_table('core_course')

        # Deleting model 'Question'
        db.delete_table('core_question')

        # Deleting model 'Answer'
        db.delete_table('core_answer')


    models = {
        'core.answer': {
            'Meta': {'object_name': 'Answer'},
            'explanation': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answer'", 'to': "orm['core.Question']"})
        },
        'core.course': {
            'Meta': {'object_name': 'Course'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        'core.exam': {
            'Meta': {'object_name': 'Exam'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        'core.question': {
            'Meta': {'object_name': 'Question'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Course']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Section']"})
        },
        'core.section': {
            'Meta': {'object_name': 'Section'},
            'exam': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Exam']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'negation': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '4', 'decimal_places': '2'})
        }
    }

    complete_apps = ['core']