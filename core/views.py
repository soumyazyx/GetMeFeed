from django.shortcuts import render
from django.http import JsonResponse
import feedparser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer, NASASerializer
from .models import Post, NASA


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'title': 'title8',
            'description': 'desc'
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
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

        # for entry in feed.entries:
        #     feed = {
        #         'link': entry.link,
        #         'title': entry.title,
        #         'author': '',
        #         'summary': entry.summary,
        #         'published': entry.published,
        #         'article_id': entry.dc_identifier,
        #         'author_img_url': entry.links[1].href,
        #         'article_img_url': entry.links[1].href
        #     }
        #     serializer = NASASerializer(data=feed)
        #     if serializer.is_valid():
        #         serializer.save()

        qs = NASA.objects.all()
        serializer = NASASerializer(qs, many=True)
        return Response(serializer.data)        

# def test_view(request):
#     data = {
#         'name':'Soumya',
#         'age': 35
#     }
#     return JsonResponse(data)


# {
#     "title": "Virginia Middle School Student Earns...", 
#     "title_detail": {
#         "type": "text/plain", 
#         "language": "en", 
#         "base": "http://www.nasa.gov/", 
#         "value": "Virginia Middle School Student Earns..."}, 
#         "links": [
#             {
#                 "rel": "alternate", 
#                 "type": "text/html", 
#                 "href": "http://www.nasa.gov/press-release/virginia-middle-school-student-earns-honor-of-naming-nasas-next-mars-rover"
#             }, 
#             {
#                 "length": "2920751", 
#                 "type": "image/png", 
#                 "href": "http://www.nasa.gov/sites/default/files/styles/1x1_cardfeed/public/thumbnails/image/2020_rover_name_plate-1080_0.png?itok=sJNPzlao", 
#                 "rel": "enclosure"
#             }
#         ], 
#         "link": "http://www.nasa.gov/press-release/virginia-middle-school-student-earns-honor-of-naming-nasas-next-mars-rover", 
#         "summary": "NASA's next Mars rover has a new name \u2013 Perseverance.", 
#         "summary_detail": {
#             "type": "text/html", 
#             "language": "en", 
#             "base": "http://www.nasa.gov/", 
#             "value": "NASA's next Mars rover has a new name \u2013 Perseverance."
#         }, 
#         "id": "http://www.nasa.gov/press-release/virginia-middle-school-student-earns-honor-of-naming-nasas-next-mars-rover", 
#         "guidislink": false, 
#         "published": "Thu, 05 Mar 2020 13:18 EST", 
#         "published_parsed": [2020, 3, 5, 18, 18, 0, 3, 65, 0], 
#         "source": {
#             "href": "http://www.nasa.gov/rss/dyn/breaking_news.rss", 
#             "title": "NASA Breaking News"
#         },
#         "dc_identifier": "458672"
#     }
            

