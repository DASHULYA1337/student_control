from django.shortcuts import get_object_or_404, render

from student_control_app.models import *


def index(request):
    curriculum = Activity.objects.all()
    return render(request, 'curriculum.html', {'curriculum': curriculum})


def teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request, 'teacher.html', {'teacher': teacher})


def subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'subject.html', {'subject': subject})


def students(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def teachers(request):
    all_teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': all_teachers})


def activity(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    marks = Mark.objects.filter(activity=activity)
    return render(request, 'activity.html', {'activity': activity, 'marks': marks})


def subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', {'subjects': subjects})
