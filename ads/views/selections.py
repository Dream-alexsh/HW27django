from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Selection
from ads.permissions import SelectionUpdatePermission
from ads.serializers.selections import SelectionSerializer, SelectionCreateSerializer, SelectionDetailSerializer, \
    SelectionUpdateSerializer, SelectionDeleteSerializer


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated]


class SelectionDetailView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDetailSerializer


class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionUpdateSerializer
    permission_classes = [IsAuthenticated, SelectionUpdatePermission]


class SelectionDeleteView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDeleteSerializer
    permission_classes = [IsAuthenticated, SelectionUpdatePermission]