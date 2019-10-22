from django.shortcuts import render


posts = [
    {
        'author': 'NFL',
        'title': 'Blog Post 1',
        'content': 'First Blog Post content Blabla Pouloulou',
        'date_posted': 'Oct 22, 2019'
    },
    {
        'author': 'JDoe',
        'title': 'Blog Post 2',
        'content': 'PouloulouPouloulouPouloulouPouloulouPouloulouPouloulou',
        'date_posted': 'Oct 23, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
