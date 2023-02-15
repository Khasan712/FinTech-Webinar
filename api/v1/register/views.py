from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.v1.register.serializers import RegisterSerializer
from api.v1.register.models import Register
from api.v1.webinar.models import Webinar


class RegisterApi(APIView):

    def post(self, request):
        try:
            params = self.request.query_params
            if not params.get('web_id'):
                return Response(
                    {
                        "status": False,
                        "error": "Send `web_id` in the params."
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            webinar = Webinar.objects.filter(uuid_webinar__uuid=params.get('web_id')).first()
            if not webinar:
                return Response(
                    {
                        'status': False,
                        'error': 'Webinar not found or inactive.'
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            serializer = RegisterSerializer(data=self.request.data)
            if not serializer.is_valid():
                return Response(
                    {
                        'status': False,
                        "error": serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save(webinar_id=webinar.id)
        except Exception as e:
            return Response(
                {
                    'status': False,
                    'error': str(e)
                }, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(
                {
                    'status': True
                }, status=status.HTTP_200_OK
            )

