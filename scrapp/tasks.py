# scraper/tasks.py
from celery import shared_task
from mainapp.models import ScrapeResult
import requests
import logging
import json

logger = logging.getLogger(__name__)

@shared_task
def scrape_proxy():
    try:
        url = 'https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc'
        response = requests.get(url)
        json_data = response.json()
        for entry in json_data['data']:
            ip = entry.get('ip', '')  
            port = entry.get('port', '')  
            protocol = entry.get('protocols', [''])[0]
            country = entry.get('country', '')  
            uptime = entry.get('upTime', '')  
            ScrapeResult.objects.create(ip=ip, port=port, protocol=protocol, country=country, uptime=uptime)
    except Exception as e:
        logger.error(f"Error occurred during scraping: {str(e)}")
