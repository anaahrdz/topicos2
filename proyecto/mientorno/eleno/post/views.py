from django.shortcuts import render
from datetime import datetime
now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs ")

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    },
    {
        'title': 'Padre e hijo',
        'user': {
            'name': 'Danielle Maclnnes',
            'picture': 'https://images.unsplash.com/profile-1449177714116-d6cac59f5eab?dpr=1&auto=format&fit=crop&w=60&h=60&q=60&crop=faces&bg=fff'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://images.unsplash.com/photo-1449177009399-be6867ef0505?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80',
    },
    {
        'title': 'Kiss in the dark',
        'user': {
            'name': 'Greg Rakozy',
            'picture': 'https://images.unsplash.com/profile-1495388545592-e4e376925c59?dpr=1&auto=format&fit=crop&w=60&h=60&q=60&crop=faces&bg=fff'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://images.unsplash.com/photo-1451444635319-e5e247fbb88d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80',
    }


]
# Create your views here.
def list_posts(request):
	return render(request, 'feed.html',{'posts':posts})