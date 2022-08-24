import json

from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView

from ads.models import Category, User, Ad


class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by('-price')

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGES)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        ads = []
        for ad in page_obj:
            ads.append({
                'id': ad.id,
                'name': ad.name,
                'author_id': ad.author_id,
                'author': ad.author.username,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published,
                'category_id': ad.category_id,
                'image': ad.image.url if ad.image else None
            })

        response = [{
            'items': ads,
            'num_pages': paginator.num_pages,
            'total': paginator.count,
        }]
        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ('name', 'author', 'price', 'description', 'category', 'is_published')

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        new_ad = Ad.objects.create(
            name=ad_data['name'],
            author=get_object_or_404(User, pk=ad_data['author_id']),
            price=ad_data['price'],
            description=ad_data['description'],
            is_published=ad_data['is_published'],
            category=get_object_or_404(Category, pk=ad_data['category_id']),
        )

        return JsonResponse({
            'id': new_ad.id,
            'name': new_ad.name,
            'author_id': new_ad.author_id,
            'author': new_ad.author.username,
            'price': new_ad.price,
            'description': new_ad.description,
            'is_published': new_ad.is_published,
            'category_id': new_ad.category_id,
            'image': new_ad.image.url if new_ad.image else None
        })


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        try:

            ad = self.get_object()

            return JsonResponse({
                'id': ad.id,
                'name': ad.name,
                'author_id': ad.author_id,
                'author': ad.author.username,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published,
                'category_id': ad.category_id,
                'image': ad.image.url if ad.image else None
            })
        except Exception:
            return JsonResponse({'error': 'Объявления не найдено'}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ('name', 'author', 'price', 'description', 'category')

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ad_data = json.loads(request.body)

        self.object.name = ad_data['name']
        self.object.author_id = ad_data['author']
        self.object.price = ad_data['price']
        self.object.description = ad_data['description']
        self.object.category_id = ad_data['category']
        self.object.image = ad_data['image']
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


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'Ok'}, status=200)


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