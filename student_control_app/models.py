from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=30)
    hours = models.PositiveSmallIntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='subject_images', blank=True, null=True)

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    subjects = models.ManyToManyField(Subject)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='teacher_images', blank=True, null=True)

    def __unicode__(self):
        return self.name


class Activity(models.Model):
    ACTIVITY_TYPES = (
        (1, 'Lesson'),
        (2, 'Workshop'),
        (3, 'Test'),
        (4, 'Laboratory'),
        (5, 'Exam')
    )
    type = models.PositiveSmallIntegerField(choices=ACTIVITY_TYPES, default=1)
    theme = models.CharField(max_length=150, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    subject = models.ForeignKey(Subject)
    teacher = models.ForeignKey(Teacher)
    classroom_number = models.PositiveSmallIntegerField(default=1)

    def __unicode__(self):
        return self.subject.name


class Student(models.Model):
    COURSES = (
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5, 'Five'),
        (6, 'Six'),
    )
    name = models.CharField(max_length=30)
    course = models.PositiveSmallIntegerField(choices=COURSES, default=1)
    subjects = models.ManyToManyField(Subject)

    def __unicode__(self):
        return self.name

    def get_average_mark(self):
        marks = Mark.objects.filter(student=self)
        average_mark = 0
        if len(marks) == 0:
            return 0
        for mark in marks:
            average_mark += mark.value
        average_mark = average_mark * 1.00 / len(marks) * 1.00
        return '%.1f' % round(average_mark, 1)

    def get_bad_marks(self):
        marks = Mark.objects.filter(student=self)
        bad_marks = 0
        for mark in marks:
            if mark.value < 3:
                bad_marks += 1
        return bad_marks


class Mark(models.Model):
    value = models.PositiveSmallIntegerField(default=3)
    activity = models.ForeignKey(Activity)
    student = models.ForeignKey(Student)

    def __unicode__(self):
        return str(self.value)

