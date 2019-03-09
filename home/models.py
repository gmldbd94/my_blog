from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#enum하고 비슷한 역할
from django.utils.translation import ugettext as _

# Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# ## 옛날 데이터베이스
# class Lecture(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField
#
# class Study(models.Model):
#     pub_date = models.DateTimeField(default=timezone.now)
#     content = models.TextField()
#     mdfile = models.FileField()
#     lecture_name = models.ForeignKey(lecture, on_delete=models.PROTECT)


#3.8 작성한 데이터베이스

class Note(TimeStampModel):
    CATEGORY = (('lecture', 'Lecture'),
                ('likelion', 'Likelion'),
                ('study', 'Study'),
                ('youtube', 'Youtube'),
                ('coding', 'Coding'),
                ('qna', 'QnA'),
                ('etc', 'etc'))
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(blank=True)
    content = models.TextField()
    category = models.CharField(choices=CATEGORY, max_length=80)
    view_count = models.IntegerField(default=0)
    link = models.URLField(blank=True)

    class Meta:
        # 생성된 날짜순으로 정령
        ordering = ['-created_at']

    @property
    def likes_count(self):
        return self.likes.all().count()

    @property
    def comment_count(self):
        return self.comments.all().count()


class Comment(TimeStampModel):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    message = models.TextField()

class Like(TimeStampModel):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.PROTECT)

class Schedule(models.Model):

    DAY_OF_THE_WEEK = {
        '1': _(u'Monday'),
        '2': _(u'Tuesday'),
        '3': _(u'Wednesday'),
        '4': _(u'Thursday'),
        '5': _(u'Friday'),
        '6': _(u'Saturday'),
        '7': _(u'Sunday'),
    }
    session = models.CharField(max_length=200)
    lecture_name = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    week = models.CharField(choices=tuple(sorted(DAY_OF_THE_WEEK.items())), max_length=1)
    table_row = models.IntegerField(default=0)

class Lecture(Note):
    schedule_id = models.ForeignKey(Schedule, on_delete=models.PROTECT)




## 수정할 내용 강의를 입력하고 매주차 강의때마다 정리할수 있는 공간을 만들자

