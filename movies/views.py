from django.shortcuts import render # type: ignore

# Create your views here.

def movie_data(request):
        movie_details = {
            'movies' : [ 
                {
                'title': 'God Father',
                'year': 1990,
                'summary': 'Comedy Entertainer',
                'success': False,
                },
                {
                'title': 'Commissioner',
                'year': 1995,
                'summary': 'Action Entertainer',
                'success': True,
                },
                {
                'title': 'Narasimham',
                'year': 1999,
                'summary': 'Family Entertainer',
                'success': True,
                }
            ]
        }
        return render(request, 'index.html', movie_details)