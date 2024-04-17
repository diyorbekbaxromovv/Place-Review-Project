from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Place, PlaceComment, Category, Meal
from django.views import View
from .forms import PlaceCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def category(request,id):
    categories = Category.objects.all()
    category = Category.objects.get(id=id)
    places = category.places.all()
    data = {
        'places': places,
        'category': category,
        'categories': categories    
    }
    
    return render(request,'food/index.html', context=data)


class PlacesListView(View):
    
    def get(self, request):
        places=Place.objects.all()
        categories = Category.objects.all()
        search_place = request.GET.get('q', '')
        
        if search_place:
            places = places.filter(name__contains=search_place)
            
        
        page_size = request.GET.get("page_size", 5)
        paginator = Paginator(places, page_size)
        page_num = request.GET.get("page", 1)
        page_object = paginator.get_page(page_num)
        
        return render(request, 'food/index.html', context={'places':page_object, "q": search_place, 'categories': categories})
    
def cat_meal(request,id):
    categories = Category.objects.all()
    category = Category.objects.get(id=id)
    places = category.places.all()
    data = {
        'places': places,
        'category': category,
        'categories': categories    
    }
    
    return render(request,'food/index.html', context=data)
    
class PlaceDetailView(DetailView):
    model = Place
    template_name = 'food/detail.html'
    context_object_name = 'food'
    pk_url_kwarg = 'id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем список блюд, относящихся к этому месту
        context['meals'] = Meal.objects.filter(place=self.object)
        # Передаем форму комментария
        context['form'] = PlaceCommentForm()
        return context



class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, id):
        place = Place.objects.get(id=id)
        comment_form = PlaceCommentForm(data=request.POST)
        
        if comment_form.is_valid():
            PlaceComment.objects.create(
                place = place,
                user = request.user,
                comment = comment_form.cleaned_data['comment'],
                stars_given = comment_form.cleaned_data['stars_given'],
            )
            return redirect(reverse('food:detail', kwargs={'id': place.id}))
        
        return render(request, 'food/detail.html', {'form': comment_form, 'place': place})
    
    


class UpdateCommentView(LoginRequiredMixin, View):
    def put(self, request, id):
        try:
            comment = PlaceComment.objects.get(id=id, user=request.user)
            comment.comment = request.POST['comment']
            comment.stars_given = request.POST['stars_given']
            comment.save()
            return JsonResponse({'success': True})
        except PlaceComment.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Comment does not exist or you do not have permission to edit it'})


class DeleteCommentView(LoginRequiredMixin, View):
    def delete(self, request, id):
        try:
            comment = PlaceComment.objects.get(id=id, user=request.user)
            comment.delete()
            return JsonResponse({'success': True})
        except PlaceComment.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Comment does not exist or you do not have permission to delete it'})
        

