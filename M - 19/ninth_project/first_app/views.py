from django.shortcuts import render
from datetime import datetime ,timedelta
from django.shortcuts import HttpResponse

# Create your views here.

#cookie:
def home(request):
    # return render(request, 'home.html')
    response = render(request , 'home.html')
    # response.set_cookie('name','rahim' , max_age=60) # ekhane max_age=60 dia bujhacche 60 sec eta thakbe. 60*3 dile 3 munite thakbe.
    response.set_cookie('name','rahim' , expires=datetime.utcnow()+timedelta(days=7))
    return response


def get_cookie(request):
    name = request.COOKIES.get('name')
    print(name)
    return render(request, 'get_cookie.html',{'name':name})

def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')
    return response



#session:

def set_session(request):
    data = {
        'name':'rahim',
        'age':25,
        'language': 'Bangla'
    }
    print(request.session.get_session_cookie_age())  # cookie koy second porjonto thakbe seta dekha jay.
    print(request.session.get_expiry_date()) #cookie koy din porjonto thakbe seta dekha jay
    request.session.update(data)
    return render(request,'home.html')


def get_session(request):
    # data = request.session
    name = request.session.get('name','Guest')
    age = request.session.get('age')
    return render(request,'get_session.html',{'name':name, 'age':age})

def delete_session(request):
    # del request.session['name']   # perticullar kichu delete kora lagle evabe .
    request.session.flush()  # full session delete kore dibe
    return render(request , 'delete_session.html')




# onekkon jabot website e kaj na korle session expired kora jay evabe.amra eta settings.py te 10 sec kore dia aschi. 
def set_session(request):                                                 #
    request.session['name'] = 'Karim'                                     #
    return render(request,'home.html')                                    #
def get_session(request):                                                 #  onekkon jabot website e kaj na korle session expired kora jay evabe
    if 'name' in request.session:                                         #
        name = request.session.get('name','Guest')  
        request.session.modified = True  # ei line ta dia bujhay protibar session er time reload korar por por 10 sec kore bartase
        return render(request,'get_session.html',{'name':name})           #
    else:                                                                 #
        return HttpResponse('Session not found')                          #