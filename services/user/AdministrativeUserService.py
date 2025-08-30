from co.edu.uco.invook.crosscutting.util import UtilNumber, UtilText
from co.edu.uco.invook.applicationcore.domain.user import AdministrativeUser, AdministrativeUserState, AdministrativeUserRole

class AdministrativeUserService:
    def create_administrative_user(self, username, password, state, role):
        username = UtilText.apply_trim(username)
        password = UtilText.apply_trim(password)
        
        admin_user = AdministrativeUser.objects.create(
            _username = username,
            _password = password,
            _state = state,
            _role = role
        )
        return admin_user