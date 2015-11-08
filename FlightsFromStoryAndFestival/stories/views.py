from django.shortcuts import render
from django.db.models import F
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from FlightsFromStoryAndFestival import settings
from stories.models import Story
from stories.serializers import StorySerializer
from stories.serializers import CustomerSerializer
from stories.serializers import PlaceSerializer
from datetime import datetime
import sys
import json
import time
import requests
from collections import OrderedDict


# Create your views here.
class StoriesViewSet(viewsets.ViewSet):
        def stories_get(self, request, user_token, format=None):
            """
            Retrieve the list of Alerts added by the user, with support for querying by metric name
            ---
            parameters:
                        - name: metric
                          required: false
                          type: string
                          paramType: query
                          description: Name / tag of the metric. When provided returns alerts corresponding to this metric name.
            """
            if user_token not in settings.ALLOWED_TOKENS:
                        return Response({'error': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)
            if request.method == 'GET' and request.query_params.get('metric') != None:
                    metric_name = request.query_params.get('metric')
                    cur_time = time.time()
                    stories = Story.objects.annotate(time_plus_freq=F('last_triggered')+F('frequency')).filter(token=user_token, rules__metric_name=metric_name, status='active', time_plus_freq__lt=cur_time).distinct()
                    serializer = StorySerializer(stories, many=True)
                    list_data = serializer.data
                    return Response(list_data)
            elif request.method == 'GET':
                        stories = Story.objects.filter(token=user_token)
            serializer = StorySerializer(stories, many=True)
            return Response(serializer.data)

        #@api_view(['POST'])
        def stories_post(self, request, user_token, format=None):
            """
                To create a new Alert
            ---
            parameters:
                        - name: body
                          required: true
                          type: "Alert"
                          paramType: body
                          description: Alert to be created.
                          value: "{some json}"
            """
            if user_token not in settings.ALLOWED_TOKENS:
                        return Response({'error': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)
            if request.method == 'POST':
                        serializer = StorySerializer(data=request.data)
                        if serializer.is_valid():
                                serializer.save()
                                return Response(serializer.data, status=status.HTTP_201_CREATED)
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def stories_detail(request, user_token, id):
        """
        Retrieve, update or delete an Alert instance.
        """
        if user_token not in settings.ALLOWED_TOKENS:
                return Response({'error': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        story = None
        try:
                story = Story.objects.get(id=id)
        except Story.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
                serializer = StorySerializer(story)
                if serializer.data['token'] == user_token:
                        return Response(serializer.data)
                else:
                        return Response({'error': 'Not allowed to access'}, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT':
                serializer = StorySerializer(story, data=request.data, partial=True)

                print "entered put criteria" , serializer
                if serializer.is_valid():
                        print "data seems to be valid"
                        if serializer.data['token'] == user_token:
                                serializer.save()
                                return Response(serializer.data)
                        else:
                                return Response({'error': 'Not allowed to access'}, status=status.HTTP_400_BAD_REQUEST)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
                serializer = StorySerializer(story)
                if serializer.data['token'] == user_token:
                        story.delete()
                        return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                        return Response({'error': 'Not allowed to access'}, status=status.HTTP_400_BAD_REQUEST)