from wallapp.models import User

class UserAuthBackend(object):

    def authenticate(self, username, password):
        try:
            user = User.objects.get(username=username)
            pwd_valid = user.check_password(password)
            if pwd_valid:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None