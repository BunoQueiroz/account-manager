from django.forms import ModelForm
from django.contrib.auth.models import User
from re import match


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = '__all__'

    def save(self, commit: bool = ...):
        
        def update_password(password: str, my_user: User):
            pattern = r'^pbkdf2_sha256\$600000\$.*=$' # TODO: create 'pattern' more especific
            if not match(pattern, password):
                my_user.set_password(password)

        def add_permissions_and_groups(permissions, groups, my_user):
            if permissions:
                for permission in permissions:
                    my_user.groups.add(permission)
            if groups:
                for group in groups:
                    my_user.groups.add(group)

        def update_user(my_user):
            my_user = model.objects.get(username=self.data.get('username'))
            my_user.username = self.data.get('username')
            my_user.first_name = self.data.get('first_name')
            my_user.last_name = self.data.get('last_name')
            my_user.email = self.data.get('email')
            permissions = self.data.get('permissions')
            groups = self.data.get('groups')
            add_permissions_and_groups(permissions, groups, my_user)
            my_user.is_staff = True if self.data.get('is_staff') is not None else False
            my_user.is_active = True if self.data.get('is_active') is not None else False
            my_user.is_superuser = True if self.data.get('is_superuser') is not None else False
            password = self.data.get('password')
            update_password(password, my_user)
            return my_user

        model = self.Meta.model
        model_in_db = model.objects.filter(username=self.data.get('username'))
        
        if model_in_db.exists():
            return update_user(model_in_db)
        
        new_user = model.objects.create_user(
            username=self.data.get('username'),
            password=self.data.get('password'),
        )
        return new_user
    
    def save_m2m(self):
        pass
