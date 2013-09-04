from django.db import models
# Models to store questions, options, answer, comment, courses.

class ExamGroup(models.Model):
    name = models.CharField(max_length = 150, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class Specialization(models.Model):
    name = models.CharField(max_length = 150, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    exam_group = models.ForeignKey(ExamGroup)
    
    def __unicode__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(max_length = 150, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    specialization = models.ForeignKey(Specialization, null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length = 150, unique=True)
    exam = models.ForeignKey(Exam)
    instructions = models.TextField()
    negation = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    
    def __unicode__(self):
        return '%s-%s' % (self.name,self.exam.name)

class Course(models.Model):
    name = models.CharField(max_length = 150, unique=True)
    
    def __unicode__(self):
        return self.name

def upload_to(instance, filename):
    return 'upload/%s/%s' % (instance.__class__.__name__,filename)

class Question(models.Model):
    description = models.TextField()
    #fig = models.FileField(upload_to=upload_to, null=True, blank=True) # only pdf
    points = models.IntegerField(default=1)
    course = models.ForeignKey(Course)
    section = models.ForeignKey(Section)
    reviewed = models.BooleanField(default=False, db_index=True)

    def __unicode__(self):
        return self.description

#class Option(models.Model):
#    question = models.ForeignKey(Question, related_name='options')
#    sl_no = models.CharField(max_length=2, choices = (
#        ('A','A'),('B','B'),('C','C'),('D','D'),('E','E')))
#    statement = models.TextField(null=True, blank=True)
#    fig = models.FileField(upload_to=upload_to, null=True, blank=True) # only pdf
#
#    def __unicode__(self):
#        return self.sl_no

class Answer(models.Model):
    question = models.OneToOneField(Question, related_name='answer')
    option = models.CharField(max_length=2, choices = (
        ('A','A'),('B','B'),('C','C'),('D','D'),('E','E')))
    explanation = models.TextField()
    #fig = models.FileField(upload_to=upload_to, null=True, blank=True) # only pdf
    
    def __unicode__(self):
        return self.option

#class Comment(models.Model):
#    question = models.ForeignKey(Question, related_name='comments')
#    comment = models.TextField()
#    user =

    
