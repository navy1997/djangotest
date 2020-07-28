from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    host = models.CharField(max_length=110)

    class Meta:
        db_table = 'project'


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.desc,
            'host': self.host
        }
