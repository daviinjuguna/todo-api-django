from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200,verbose_name="title")
    description = models.TextField(verbose_name="description")
    complete = models.BooleanField(default=False, blank=True, null=True,verbose_name="complete")
    when_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False)
    when_modified = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "todo"
        verbose_name = "Todo"
        verbose_name_plural = "Todos"