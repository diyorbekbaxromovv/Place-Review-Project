from django.core.paginator import Paginator
from django.views import View
from food.models import PlaceComment
from django.shortcuts import render


class HomeView(View):
    def get(self, request):
        place_reviews = PlaceComment.objects.all().order_by('-created_at')
        page_size = request.GET.get('page_size', 2)
        paginator = Paginator(place_reviews, page_size)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        
        return render(request, 'food/feed.html', {'place_reviews':page_obj})