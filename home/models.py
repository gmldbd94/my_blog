from django.db import models
from django.utils import timezone
# Create your models here.
class lecture(models.Model):
    title = models.CharField(max_length=200)
    when = models.CharField()
    description = models.TextField


class study(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    mdfile = models.FileField()
    lecture_name = models.ForeignKey(lecture)

## 수정할 내용 강의를 입력하고 매주차 강의때마다 정리할수 있는 공간을 만들자

