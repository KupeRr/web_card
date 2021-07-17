from django.shortcuts import render
 
def method(request):
    data = {
        'title':'Главная страница',
        'skills':['Python', 'java', 'C++'],
        'data_about':{
            'name':'Никита',
            'surname':'Шеломенцев',
            'age':'21',
            'pos':'Software Engineer',
            'part_pos':'Фрилансер/Репетитор'
        }
    }

    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    contacts = {
        'Telegram':'@KupeRRRR',
        'Freelance':'KupeRr',
        'GitHub':'KupeRr',
    }
    return render(request, 'main/contact_home.html', contacts)