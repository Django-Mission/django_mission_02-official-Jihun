from django.contrib import admin

from .models import Faq, Inquiry, Answer

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('content', 'category', 'writer', 'answer', 'created_at', 'last_modifier', 'modifed_at')
    list_filter = ('created_at',)
    
    search_fields = ('id', 'writer__username')
    search_help_text = '계시판 번호, 작성자 검색이 가능합니다'

    def save_model(self, request, obj, form, change):
        if not obj.writer:
            obj.writer = request.user
        obj.last_modifier = request.user
        obj.save()


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'writer', 'e_mail', 'phone_number', 'content', 'image', 'created_at', 'modifed_at')
    list_filter = ('created_at',)
    
    search_fields = ('id', 'writer__username')
    search_help_text = '계시판 번호, 작성자 검색이 가능합니다'

    def save_model(self, request, obj, form, change):
        if not obj.writer:
            obj.writer = request.user
        obj.last_modifier = request.user
        obj.save()

    inlines = [AnswerInline]


