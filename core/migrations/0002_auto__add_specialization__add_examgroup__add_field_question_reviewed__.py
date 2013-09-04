# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Specialization'
        db.create_table('core_specialization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('exam_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ExamGroup'])),
        ))
        db.send_create_signal('core', ['Specialization'])

        # Adding model 'ExamGroup'
        db.create_table('core_examgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('core', ['ExamGroup'])

        # Adding field 'Question.reviewed'
        db.add_column('core_question', 'reviewed',
                      self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True),
                      keep_default=False)

        # Adding field 'Exam.specialization'
        db.add_column('core_exam', 'specialization',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Specialization'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Specialization'
        db.delete_table('core_specialization')

        # Deleting model 'ExamGroup'
        db.delete_table('core_examgroup')

        # Deleting field 'Question.reviewed'
        db.delete_column('core_question', 'reviewed')

        # Deleting field 'Exam.specialization'
        db.delete_column('core_exam', 'specialization_id')


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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'specialization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Specialization']", 'null': 'True', 'blank': 'True'})
        },
        'core.examgroup': {
            'Meta': {'object_name': 'ExamGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        'core.question': {
            'Meta': {'object_name': 'Question'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Course']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Section']"})
        },
        'core.section': {
            'Meta': {'object_name': 'Section'},
            'exam': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Exam']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'negation': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '4', 'decimal_places': '2'})
        },
        'core.specialization': {
            'Meta': {'object_name': 'Specialization'},
            'exam_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ExamGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        }
    }

    complete_apps = ['core']