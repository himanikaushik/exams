# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404
from core.models import *


def home(request):
    try:
        if request.method == 'GET':
            exam_groups = ExamGroup.objects.all()
            context_dict = {'exam_groups':exam_groups}
            return render_to_response('index.html', context_dict,
                context_instance = RequestContext(request))
    except:
        raise Http404
        

def exam_group(request, exam_group):
    try:
        if request.method == 'GET':
            exam_groups = ExamGroup.objects.all()
            specializations = Specialization.objects.select_related(
                'exam_group').filter(exam_group__slug=exam_group)
            context_dict = {'specializations':specializations,
                'exam_groups':exam_groups}
            return render_to_response('exam_group.html', context_dict,
                context_instance = RequestContext(request))
    except:
        raise Http404

def specialization(request, exam_group, specialization):
    try:
        if request.method == 'GET':
            exam_groups = ExamGroup.objects.all()
            exams = Exam.objects.select_related('specialization',
                'specialization__exam_group').filter(specialization__slug=specialization,
                specialization__exam_group__slug=exam_group)
            context_dict = {'exam_groups':exam_groups, 'exams':exams}
            return render_to_response('specialization.html', context_dict,
                context_instance = RequestContext(request))
    except:
        raise Http404

def exam(request, exam_group, specialization, exam):
    try:
        if request.method == 'GET':
            exam_groups = ExamGroup.objects.all()
            questions = Question.objects.select_related('section',
                'section__exam','section__exam__specialization').filter(
                section__exam__specialization__slug=specialization)
            context_dict = {'exam_groups':exam_groups, 'questions':questions}
            return render_to_response('exam.html', context_dict,
                context_instance = RequestContext(request))
    except Exception, e:
        print repr(e)
        raise Http404
