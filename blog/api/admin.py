from django.contrib import admin
from api.models import Post
# Register your models here.
from .models import Post

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_content','author','updated_at','created_at')

    def short_content(self, obj):
        # Ensure obj.content is properly fetched
        if obj.content:
            words = obj.content.split()[:10]  # Split content and take first 10 words
            truncated_content = ' '.join(words)
            if len(obj.content.split()) > 10:
                truncated_content += ' ......'  # Append '...' if content is longer
            return truncated_content
        return ''  # Return an empty string if no content

        short_content.short_description = 'Content'  # Column header


admin.site.register(Post,CompanyAdmin)
