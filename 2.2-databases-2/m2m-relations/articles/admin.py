from django.contrib import admin
from .models import Tag, Scope, Article
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

# class ScopeInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         for form in self.forms:
#             # form.cleaned_data
#             # print(form.cleaned_data)
#             if form.cleaned_data['is_main'] is True:
#             #      raise ValidationError('Тут всегда ошибка')
#                 raise ValidationError('Тут всегда ошибка')
#         return super().clean()



class ScopeInline(admin.TabularInline):
    model = Scope
    extre = 0
    #formset = ScopeInlineFormset

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    tage_name = ['id','name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
       inlines = [ScopeInline]
