from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Basch_the_Strong',
        'title': 'More remedies?',
        'content': 'Where can I find a caster that knows Remedy? Need to kill a wraith.',
        'date_posted': 'May 2 2020'
    },
    {
        'author': 'VaanBro_92',
        'title': 'RE: More remedies?',
        'content': 'Basch, that bounty isn\'t going anywhere, we\'ll get back to Rabanaster soon enough.',
        'date_posted': 'May 2 2020'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

