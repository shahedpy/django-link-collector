import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import ScrapedLink
import pandas as pd
import io


def index(request):
    links = ScrapedLink.objects.all().order_by('-id')
    return render(request, 'scraper/index.html', {'links': links})


def scrape(request):
    if request.method == "POST":
        site_url = request.POST.get('site_url')
        if site_url:
            try:
                page = requests.get(site_url)
                soup = BeautifulSoup(page.text, 'html.parser')

                for link in soup.find_all('a'):
                    link_address = link.get('href')
                    link_text = link.string
                    if link_address:
                        ScrapedLink.objects.create(
                            name=link_text, address=link_address)
            except Exception as e:
                print(f"Error scraping: {e}")

    return redirect('/')


def clear_links(request):
    ScrapedLink.objects.all().delete()
    return redirect('/')


def download_links(request):
    format_type = request.GET.get('format')
    links = ScrapedLink.objects.all().values('id', 'name', 'address')
    df = pd.DataFrame(list(links))

    if format_type == 'CSV':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="links.csv"'
        df.to_csv(path_or_buf=response, index=False)
        return response

    elif format_type == 'XLSX':
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
        response = HttpResponse(
            output.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')  # noqa:E501
        response['Content-Disposition'] = 'attachment; filename="links.xlsx"'
        return response

    elif format_type == 'JSON':
        data = list(links)
        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})

    return redirect('/')
