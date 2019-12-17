from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db import models
from martor.widgets import AdminMartorWidget
from apps.translation.admin import TranslatedTextInlineLarge , TranslatedTextInlineSmall

from apps.blog.models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(ModelAdmin):
    fields = ()
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

    inline_type = 'stacked'
    inline_reverse = [
        {
            'field_name': 'post_title',
            'kwargs': {},
            'admin_class': TranslatedTextInlineSmall
        },
        {
            'field_name': 'post_description',
            'kwargs': {},
            'admin_class': TranslatedTextInlineLarge
        },
        {
            'field_name': 'text',
            'kwargs': {},
            'admin_class': TranslatedTextInlineLarge
        },
    ]
    pass


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    comment_shown_editable = ['shown']
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    pass


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    pass
