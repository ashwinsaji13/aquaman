from django.conf import settings
from requests import Response
from rest_framework import pagination


class YourPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
               'next': self.get_next_link(),
               'previous': self.get_previous_link(),
               'count': self.page.paginator.count,
               'total_pages': self.page.paginator.num_pages,
               'results': data
        })


