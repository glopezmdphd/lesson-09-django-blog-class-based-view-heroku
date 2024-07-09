from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Post.categories.through
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    list_display = ("title", "author", "published_date")
    search_fields = ["title", "text"]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
