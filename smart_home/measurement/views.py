from rest_framework.generics import RetrieveUpdateDestroyAPIView, GenericAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer


class SensorView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorDetailSerializer(sensors, many=True)
        return Response(ser.data)

    def post(self, request):
        new_sensor = Sensor.objects.get_or_create(name='ESP32', description="Датчик над входной дверью")
        if not new_sensor[1]:
            return Response({'status': 'Датчик с такими параметрами уже сществует'})
        else:
            ser = SensorDetailSerializer(new_sensor[0])
            return Response(ser.data)


class SensorIdView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementsView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def get(self, request):
        return self.list(request)

    def perform_create(self, serializer):
        sensor = get_object_or_404(Sensor, id=self.request.data.get('id_sensor'))
        return serializer.save(id_sensor=sensor)

    def post(self, request):
        return self.create(request)


