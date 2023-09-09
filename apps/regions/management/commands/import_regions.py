import json
from django.conf import settings
from django.core.management.base import BaseCommand

from apps.regions.models import Region


class Command(BaseCommand):
    help = 'Import regions from JSON'

    def handle(self, *args, **kwargs):
        with (
            open(f"{settings.BASE_DIR}/apps/regions/management/commands/regions.json",
                 encoding="latin-1") as regions_json_file,
            open(f"{settings.BASE_DIR}/apps/regions/management/commands/districts.json",
                 encoding="latin-1") as districts_json_file,
            open(f"{settings.BASE_DIR}/apps/regions/management/commands/villages.json",
                 encoding="latin-1") as villages_json_file
        ):
            regions_data = json.load(regions_json_file)
            districts_data = json.load(districts_json_file)
            villages_data = json.load(villages_json_file)
            for region_data in regions_data:
                region, _ = Region.objects.get_or_create(name=region_data.get("name_uz"))
                for district_data in self.get_filtered_regions(districts_data, region_data.get("id")):
                    district, _ = Region.objects.get_or_create(name=district_data.get("name_uz"), defaults={"parent": region})
                    for village_data in self.get_filtered_regions(villages_data, district_data.get("id"), "villages"):
                        Region.objects.get_or_create(name=village_data.get("name_uz"), defaults={"parent": district})

        self.stdout.write(self.style.SUCCESS('Successfully added regions, districts and villages'))

    @staticmethod
    def get_filtered_regions(data, parent_id, type_="districts"):
        return [
            row
            for row in data
            if row.get("region_id" if type_ == "districts" else "district_id") == parent_id
        ]
