from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.db import connections

class DynamicDatabaseUserMiddleware:
    def __call__(self, request):
        if request.user.is_authenticated:
            user_role = request.user.role
            if user_role == 'waiter':
                self.set_mongo_credentials('waiter_mongo', 'waiter_mongo_password')
                self.set_postgres_credentials('waiter', 'waiter_password')
            elif user_role == 'chef':
                self.set_mongo_credentials('chef_mongo', 'chef_mongo_password')
                self.set_postgres_credentials('chef', 'chef_password')

        response = self.get_response(request)
        return response

    def set_postgres_credentials(self, username, password):
        db_conn = connections['postgres']
        db_conn.settings_dict['USER'] = username
        db_conn.settings_dict['PASSWORD'] = password
        db_conn.close()  # Reconnect using new credentials

    def set_mongo_credentials(self, username, password):
        db_conn = connections['mongo']
        db_conn.settings_dict['CLIENT']['username'] = username
        db_conn.settings_dict['CLIENT']['password'] = password
        db_conn.close()  # Reconnect using new credentials


class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Extract token from the "access_token" cookie
        token = request.COOKIES.get('access_token')
        if token is None:
            return None

        try:
            validated_token = self.get_validated_token(token)
            return self.get_user(validated_token), validated_token
        except AuthenticationFailed:
            return None
