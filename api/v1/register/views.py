from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.v1.register.serializers import RegisterSerializer
from api.v1.register.models import Register
from api.v1.webinar.models import Webinar


# class RegisterApi(APIView):
#
#     def post(self, request):
#         try:
#             params = self.request.query_params
#             if not params.get('web_id'):
#                 serializer = RegisterSerializer(data=self.request.data)
#                 if not serializer.is_valid():
#                     return Response(
#                         {
#                             'status': False,
#                             "error": serializer.errors
#                         }, status=status.HTTP_400_BAD_REQUEST
#                     )
#                 serializer.save()
#                 return Response(
#                     {
#                         'status': True
#                     }, status=status.HTTP_200_OK
#                 )
#             webinar = Webinar.objects.filter(uuid_webinar__uuid=params.get('web_id')).first()
#             if not webinar:
#                 return Response(
#                     {
#                         'status': False,
#                         'error': 'Webinar not found or inactive.'
#                     }, status=status.HTTP_400_BAD_REQUEST
#                 )
#             serializer = RegisterSerializer(data=self.request.data)
#             if not serializer.is_valid():
#                 return Response(
#                     {
#                         'status': False,
#                         "error": serializer.errors
#                     }, status=status.HTTP_400_BAD_REQUEST
#                 )
#             serializer.save(webinar_id=webinar.id)
#         except Exception as e:
#             return Response(
#                 {
#                     'status': False,
#                     'error': str(e)
#                 }, status=status.HTTP_400_BAD_REQUEST
#             )
#         else:
#             return Response(
#                 {
#                     'status': True
#                 }, status=status.HTTP_200_OK
#             )


class RegisterApi(APIView):
    def post(self, request):
        try:
            data = self.request.data
            course = data.get('course')
            first_name = data.get('first_name')
            phone_number = data.get('phone_number')

            if not first_name or not phone_number:
                return Response(
                    {
                        "status": False,
                        "error": "Name or Phone not given!"
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            serializer = RegisterSerializer(data=data)
            if not serializer.is_valid():
                return Response(
                    {
                        'status': False,
                        "error": serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            if course:
                if course not in ['backend', 'frontend', 'mobile']:
                    return Response(
                        {
                            "status": False,
                            "error": "Course not found!!!"
                        }
                    )
                serializer.save(course=course)
            else:
                serializer.save(course='webinar')
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
                }, status=status.HTTP_201_CREATED
            )




