from django_registration.forms import RegistrationForm
from .models import UserModel

class UserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']  # List the fields you want in the form
