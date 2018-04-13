from django.contrib.auth.forms import UserCreationForm as DefaultUserCreationForm
from accounts.models import User

class UserCreationForm(DefaultUserCreationForm):
    class Meta(DefaultUserCreationForm.Meta):
        model = User
        fields = DefaultUserCreationForm.Meta.fields + ('email',) # add new custom fields