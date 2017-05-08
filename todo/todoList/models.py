from django.db import models


class Todo(models.Model):
    todo_text = models.CharField(max_length=159)
    deadline_date = models.DateTimeField('date published')
    percentage = models.IntegerField(default=0)
    def __str__(self):
        return self.todo_text
