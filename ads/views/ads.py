from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.models import Ad
from ads.serializers.ads import AdSerializer, AdCreateSerializer, AdUpdateSerializer, AdDeleteSerializer


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        category = request.GET.get('cat', None)
        if category:
            self.queryset = self.queryset.filter(
                category__in=category
            )
        text = request.GET.get('text', None)
        if text:
            self.queryset = self.queryset.filter(
                name__icontains=text
            )
        location = request.GET.get('location', None)
        if location:
            self.queryset = self.queryset.filter(author__locations__name__icontains=location)
        price_from = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().get(request, *args, **kwargs)


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDeleteSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ('name', 'author', 'price', 'description', 'category', 'image')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES['image']
        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'author_id': self.object.author_id,
            'author': self.object.author.username,
            'price': self.object.price,
            'description': self.object.description,
            'is_published': self.object.is_published,
            'category_id': self.object.category_id,
            'image': self.object.image.url if self.object.image else None
        })