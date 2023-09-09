from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from mptt.admin import DraggableMPTTAdmin

from apps.regions.models import Region


class RegionFilter(SimpleListFilter):
    title = 'region'
    parameter_name = 'parent_id'

    def lookups(self, request, model_admin):
        regions = set([region for region in model_admin.model.objects.filter(parent__isnull=True)])
        return [(region.id, region.name) for region in regions]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(parent_id=self.value())


@admin.register(Region)
class RegionAdmin(DraggableMPTTAdmin):
    search_fields = ['name']
    list_filter = [RegionFilter]
    list_display = ('tree_actions', 'indented_title')
