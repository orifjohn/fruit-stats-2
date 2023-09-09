from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404

from apps.regions.models import Region


def region_detail(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    children = Region.objects.filter(parent=region)
    page = request.GET.get('page', 1)
    paginator = Paginator(children, 10)

    try:
        children = paginator.page(page)
    except EmptyPage:
        children = paginator.page(paginator.num_pages)

    return render(request, 'pages/region_detail.html', {'region': region, 'children': children})
