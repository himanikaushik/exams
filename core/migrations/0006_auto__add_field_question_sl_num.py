# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Question.sl_num'
        db.add_column('core_question', 'sl_num',
                      self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Question.sl_num'
        db.delete_column('core_question', 'sl_num')


    models = {
        'core.answer': {
            'Meta': {'object_name': 'Answer'},
            'explanation': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'question': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'answer'", 'unique': 'True', 'to': "orm['core.Question']"})
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'specialization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Specialization']", 'null': 'True', 'blank': 'True'})
        },
        'core.examgroup': {
            'Meta': {'object_name': 'ExamGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'core.question': {
            'Meta': {'object_name': 'Question'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Course']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Section']"}),
            'sl_num': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'core.section': {
            'Meta': {'object_name': 'Section'},
            'exam': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Exam']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'negation': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '4', 'decimal_places': '2'})
        },
        'core.specialization': {
            'Meta': {'object_name': 'Specialization'},
            'exam_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ExamGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']