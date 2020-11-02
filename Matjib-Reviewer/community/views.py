from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews':reviews
    }

    return render(request, 'review_list.html', context)


def new_review(request):
    return render(request, 'new_review.html')


def create_review(request):
    review = Review()

    review.title = request.POST.get('title')
    review.rank = request.POST.get('rank')
    review.content = request.POST.get('content')

    review.save()

    return redirect('community:index')


def review_detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review':review
    }
    return render(request, 'review_detail.html', context)

