from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', ]
        # fields = '__all__'