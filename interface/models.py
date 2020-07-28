from django.db import models
from es.models import Project

# Create your models here.
class Interface(models.Model):
    name = models.CharField(max_length=255,null=True)
    desc = models.CharField(max_length=255,null=True)
    project = models.ForeignKey(Project,to_field='id',on_delete=models.CASCADE)

    class Meta:
        db_table = 'interface'

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "desc":self.desc,
            "project":self.project.id
        }
