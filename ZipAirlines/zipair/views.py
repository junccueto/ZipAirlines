from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

import math
# Create your views here.

class Assess_Planes(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request: HttpRequest) -> Response:
        data = request.data

        if not isinstance(data, list):
            return Response({'message': 'Bad Request: Data should be a list of airplane data.'},
                            status=status.HTTP_400_BAD_REQUEST)

        if len(data) == 10:
            return_data = []

            for plane_data in data:
                a_id = plane_data.get('id', None)
                passengers = plane_data.get('passengers', None)

                if a_id and passengers and isinstance(a_id, int) and isinstance(passengers, int):
                    fuel_tank = 200 * a_id
                    consumption = 0.80 * (math.log(a_id) / math.log(10))
                    pass_consumption = 0.002 * passengers

                    total_consumption = consumption + pass_consumption
                    max_flight_time = fuel_tank / total_consumption

                    plane_stats = {
                        'id': a_id,
                        'passengers': passengers,
                        'fuel_tank_capacity': fuel_tank,
                        'fuel_consumption_per_minute': total_consumption,
                        'max_flight_time': max_flight_time
                    }

                    return_data.append(plane_stats)
                else:
                    return Response({'message': 'Bad Request: Data error for aiplane with id {0}'.format(a_id)},
                                    status=status.HTTP_400_BAD_REQUEST)

            return Response(return_data)
        else:
            return Response({'message': 'Bad Request: Must process 10 airplanes'},
                             status=status.HTTP_400_BAD_REQUEST)
