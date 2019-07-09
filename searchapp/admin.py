from django.contrib import admin #adminサイトテンプレ読み込み
from .models import GoodsTBL #model定義TBL読み込み
from .models import CategoryTBL #model定義TBL読み込み
from .models import HighCategoryTBL #model定義TBL読み込み



#adminサイトのメソッドで以下TBL登録

'''
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('goodsid','categoryname','sizename','colorname','goodsname')
    def categoryname(self,obj):
        return obj.categoryid.categoryname
    categoryname.short_description = 'categoryname'
'''

admin.site.register(GoodsTBL)
admin.site.register(CategoryTBL)
admin.site.register(HighCategoryTBL)