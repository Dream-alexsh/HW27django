import json

from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView

from ads.models import User


class UserListView(ListView):
    model = User
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.prefetch_related("locations").annotate(
            total_ads=Count('ad__is_published', filter=Q(ad__is_published=True))
        ).order_by('username')

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGES)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        users = []
        for user in page_obj:
            users.append({
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'role': user.role,
                'age': user.age,
                'locations': list(user.locations.all().values_list('name', flat=True)),
                'total_ads': user.total_ads,
            })

        response = [{
            'items': users,
            'num_pages': paginator.num_pages,
            'total': paginator.count,
        }]
        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'role', 'age', 'locations')

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        new_user = User.objects.create(
            username=user_data['username'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            role=user_data['role'],
            age=user_data['age'],
        )

        return JsonResponse({
            'id': new_user.id,
            'username': new_user.username,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'role': new_user.role,
            'age': new_user.age,
            'locations': list(new_user.locations.all().values_list('name', flat=True))
        })


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        try:

            user = self.get_object()

            return JsonResponse({
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'role': user.role,
                'age': user.age,
                'locations': list(user.locations.all().values_list('name', flat=True))
            })
        except Exception:
            return JsonResponse({'error': 'Пользователь не найден'}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'role', 'age', 'locations')

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)

        self.object.username = user_data['username']
        self.object.first_name = user_data['first_name']
        self.object.last_name = user_data['last_name']
        self.object.role = user_data['role']
        self.object.age = user_data['age']
        self.object.locations = user_data['locations']
        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'username': self.object.username,
            'first_name': self.object.first_name,
            'last_name': self.object.last_name,
            'role': self.object.role,
            'age': self.object.age,
            'locations': list(self.object.locations.all().values_list('name', flat=True))
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'Ok'}, status=200)
