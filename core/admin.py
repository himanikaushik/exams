from django.contrib import admin
from core.models import *

class CoreExamAdmin(admin.ModelAdmin):
    model = Exam
admin.site.register(Exam,CoreExamAdmin)

class CoreSectionAdmin(admin.ModelAdmin):
    model = Section
admin.site.register(Section,CoreSectionAdmin)

class CoreCourseAdmin(admin.ModelAdmin):
    list_display = ['name']
    #list_filter = ['position']
admin.site.register(Course,CoreCourseAdmin)

#class CoreTopicAdmin(admin.ModelAdmin):
#    model = Topic
#admin.site.register(Topic,CoreTopicAdmin)

#class CoreOptionInline(admin.StackedInline):
#    model = Option
#    max_num = 4 
#    extra = 4

class CoreAnswerInline(admin.StackedInline):
    model = Answer
    max_num = 1

class CoreQuestionAdmin(admin.ModelAdmin):
    #fields = ['description','course','topic','fig']
    model = Question
    inlines = [CoreAnswerInline]
    
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]

admin.site.register(Question,CoreQuestionAdmin)

#class CoreAnswerAdmin(admin.ModelAdmin):
#    model = Answer
#    
#    class Media:
#        js = [
#            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
#            '/static/grappelli/tinymce_setup/tinymce_setup.js',
#        ]
#
#admin.site.register(Answer,CoreAnswerAdmin)

