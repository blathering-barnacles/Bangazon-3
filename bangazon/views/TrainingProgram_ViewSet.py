from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from bangazon.models import TrainingProgram
from bangazon.serializers import TrainingProgramSerializer
from django.shortcuts import render
from rest_framework import filters
from rest_framework import status
import datetime






class TrainingProgramViewSet(viewsets.ModelViewSet):
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer

    filter_backends = (filters.SearchFilter, )
    search_fields = ('id', 'name', 'startDate', 'endDate', 'maxAttendees', 'deletedOn', 'url')

    def get_queryset(self):
        print("TIME: ", str(datetime.datetime.now())[0:10])
        # today = str(datetime.datetime.now())[0:10]
        today = datetime.datetime.now()
        query_set = TrainingProgram.objects.all()
        # print("query", query_set[0])
        keyword = self.request.query_params.get('completed', None)

        if keyword == "false":
            query_set = query_set.filter(startDate__gte=today)
        elif keyword == "true":
            query_set = query_set.filter(endDate__lte=today)
        elif keyword is not None:
            query_set = query_set.filter(startDate__gte=today)

        return query_set


