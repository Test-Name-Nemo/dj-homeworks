from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, ArticleTags


class ArticleTagsInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        if counter < 1:
            for form in self.forms:
                data = form.cleaned_data
                if data.get('is_main'):
                    counter += 1
        else:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean()


class ArticleTagsInline(admin.TabularInline):
    model = ArticleTags
    formset = ArticleTagsInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagsInline]