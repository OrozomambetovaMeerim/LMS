from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(User, 
                                related_name='courses_created',
                                on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,
                                related_name='courses_created',
                                on_delete=models.CASCADE)     
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)  
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course,
                                related_name='courses_created',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Content(models.Model):
    module = models.ForeignKey(Module,
                                related_name='contents',
                                on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                        on_delete=models.CASCADE,
                                        limit_choices_to={'model_in':(
                                            'text',
                                            'file',
                                            'image',
                                            'video')}) 
    object_id = models.PositiveIntegerField()
    item = 	GenericForeignKey('content_type', 'object_id')


class ItemBase(models.Model):
    owner = models.ForeignKey(User,
                                related_name='%(class)s_related', 
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def	__str__(self):
        return  self.title

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')                                            

class Image(ItemBase):
    file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()


user = models.ForeignKey(
    to=User,
    on_delete=models.SET_NULL,
    null=True, blank=True,
)




class Student(models.Model):
    first_name = models.CharField(max_length=100, null=True, default=' ')
    last_name = models.CharField(max_length=100, null=True, default=' ')
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    image = models.ImageField(null=True)
    student_id = models.CharField(max_length=15, null=True, default=' ')
    Course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    Subject = models.ManyToManyField(Subject)


    # def Student(request):
    #     student_list = Student.objects.all()
    #     return (request, "student.html")

    def	__str__(self):
        return  self.name

    def get_courses(self):
        course_list = self.courses.all()
        return course_list

    def get_subject(self):
        subject_list = self.get_subject()
        courses = subject_list.none()
        for cls in subject_list:
            subject = subject | cls.get_subjects()
        return subject

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class Teacher(models.Model):
    fname = models.CharField(max_length=100, null=True, default=' ')
    lname = models.CharField(max_length=100, null=True, default=' ')
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=15, null=True, default=' ')
    Course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    Subject = models.ManyToManyField(Subject)

    def __str__(self):
        return str(self.fname) + ' ' + str(self.lname)


class Homework(models.Model):
    name = models.CharField(max_length=250, null=True, default=' ')
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    relate_class = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Exam(models.Model):
    name = models.CharField(max_length=250, null=True, default=' ')
    date = models.DateTimeField(null=True)
    relate_class = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class HomeworkAnswer(models.Model):
    description = models.CharField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    file = models.FileField()
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)

class Student_answer(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    subject_title = models.CharField(max_length=30, blank=True)
    answer = models.TextField(blank=True)