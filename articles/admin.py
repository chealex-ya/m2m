from django.contrib import admin

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag']

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_list = []
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if not form.cleaned_data:
                raise ValidationError('Нужен хотя бы один тег')
            else:
                try:
                    is_main_list.append(form.cleaned_data['is_main'])
                    if True in is_main_list:
                        pass
                    else:
                        raise ValidationError('Хотя бы один тег должен быть основным')
                except KeyError:
                    pass
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    list_display = ['id', 'tag', 'is_main']
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'published_at', 'image']
    inlines = [ScopeInline]