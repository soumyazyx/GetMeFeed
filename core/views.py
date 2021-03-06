
# Change log
# 20200308 Soumya Added feed for space.com
# 20200308 Soumya Added BeautifulSoup to scrap summary from space.com 

from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import feedparser
import re
import requests 
from bs4 import BeautifulSoup
# Import rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer, NASASerializer, SPACEDOTCOMSerializer
from .models import Post, NASA, SPACEDOTCOM


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class NASAView(APIView):
    def get(self, request, *args, **kwargs):
        feed = feedparser.parse('https://www.nasa.gov/rss/dyn/breaking_news.rss')
        for entry in feed.entries:
            obj, created = NASA.objects.get_or_create(
                link=entry['link'],
                title=entry['title'],
                author=feed['feed']['author'],
                summary=entry['summary'],
                published=entry['published'],
                article_id=entry['dc_identifier'],
                author_img_url='',
                article_img_url=entry['links'][1]['href']
            )

        qs = NASA.objects.all()
        serializer = NASASerializer(qs, many=True)
        return Response(serializer.data)        


class SPACEDOTCOMView(APIView):
    def get(self, request, *args, **kwargs):
        article_img_url = ''
        feed = feedparser.parse('https://www.space.com/feeds/all')
        for entry in feed.entries:
            for link in entry['links']:
                if ('image' in link.type):
                    article_img_url = link.href
            # Space.com doesnt provide the summary content
            # So, use beautiful soup to scrap the article
            # We are fetching the 'complete' sentences within 500char limit
            r = requests.get(entry['link'])
            htmlContent = r.content
            soup = BeautifulSoup(htmlContent, 'html.parser')
            summary = str(soup.find(id="article-body").get_text())[0:500].split(".")
            summary.pop()
            summary = ".".join(summary)


            obj, created = SPACEDOTCOM.objects.get_or_create(
                link=entry['link'],
                title=entry['title'],
                author=entry['author'],
                summary=summary,
                published=entry['published'],
                published_parsed=entry['published_parsed'],
                article_id='',
                author_img_url='',
                article_img_url=article_img_url
            )

        qs = SPACEDOTCOM.objects.all()
        serializer = SPACEDOTCOMSerializer(qs, many=True)
        return Response(serializer.data)        


def dummy(request):
    return JsonResponse({
        'author': 'Soumya',
        'NASA': '/NASA',
        'SPACEDOTCOM': '/SPACEDOTCOM'
    }, safe=False)
