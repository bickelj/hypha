import re

from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import Http404
from django.shortcuts import render
from wagtail.core.models import Page
from wagtail.search.models import Query

from hypha.public.home.models import HomePage


def search(request):
    if request.site != HomePage.objects.first().get_site():
        raise Http404

    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)

    # Search
    if search_query:
        # Allow only word characters and spaces in search query.
        words = re.findall('\w+', search_query.strip())
        search_query = ' '.join(words)

        public_site = request.site.root_page

        search_results = Page.objects.live().descendant_of(
            public_site,
            inclusive=True,
        ).specific().search(search_query, operator='and')
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, settings.DEFAULT_PER_PAGE)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })