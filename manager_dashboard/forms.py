from django.contrib.auth.models import User

class UserActiveStatusForm(forms.Form):
    class Meta:
        model = User
        fields = ('is_active')

class UserRoleForm(forms.Form):
    class Meta:
        model = User
        fields = ('is_staff')