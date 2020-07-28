from django.db import models
from interface.models import Interface

# Create your models here.
class Case(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255,null=True)
    uri = models.CharField(max_length=116)
    header = models.CharField(max_length=255,null=True)
    body = models.CharField(max_length=255,null=True)
    r_type = models.CharField(max_length=255,null=False)
    result = models.CharField(max_length=255,null=False)
    interface = models.ForeignKey(Interface,to_field='id',on_delete=models.CASCADE)

    class Meta:
        db_table = 'case'

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "desc":self.desc,
            "uri":self.uri,
            "header":self.header,
            "body":self.body,
            "r_type":self.r_type,
            "result":self.result,
            "interface":self.interface.id
        }