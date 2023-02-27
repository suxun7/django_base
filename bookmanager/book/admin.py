from django.contrib import admin
from book.models import BookInFo,PersonInFo
# Register your models here.
#注册模型类
admin.site.register(BookInFo)
admin.site.register(PersonInFo)
#重新运行django