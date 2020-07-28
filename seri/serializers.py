from rest_framework import serializers

from seri.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def create(self,data):
        book = Student.objects.create(**data)  # 利用 解包, 传入对应的键值对
        return book  # 记得必须返回 book对象