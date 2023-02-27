from django.db import models

# Create your models here.

"""
1.我们的模型类需要继承自 models.Model
2.系统会自动为我们添加一个主键--id
3.字段
    字段名=model.类型（选项）
    字段名就是数据表的字段名
    字段名不要使用python，mysql等关键字
    
    char（m）
    varchar（m）
    m就是选项
"""
"""
1.定义模型类
2.模型迁移
    1.生成迁移文件：根据模型类生成创建表的语句
    python manage.py makemigrations
    2.执行迁移：根据第一步生成的语句在数据库中创建表
    python manage.py migrate
3.操作数据库
"""


class BookInFo(models.Model):#Book类继承models.Model
    #id
    name=models.CharField(max_length=10)

class PersonInFo(models.Model):
    name=models.CharField(max_length=10)
    gender=models.BooleanField()
    #外键约束：任务属于哪本书
    age=models.ForeignKey(BookInFo,on_delete=models.CASCADE)
