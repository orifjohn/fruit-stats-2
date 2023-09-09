from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render

from apps.regions.models import Region


def fruit_statistics(request):
    regions = Region.objects.root_nodes()
    page = request.GET.get('page', 1)
    paginator = Paginator(regions, 20)

    try:
        regions = paginator.page(page)
    except EmptyPage:
        regions = paginator.page(paginator.num_pages)

    return render(request, 'pages/home.html', {'regions': regions})
