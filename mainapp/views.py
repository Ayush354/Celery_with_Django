from scrapp.tasks import scrape_proxy
from django.http import HttpResponse


def test(request):
    scrape_proxy()
    return HttpResponse("Done")
