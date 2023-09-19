from userManagement.utill.ResponseEntity import ResponseEntity

class UserController:

    @staticmethod
    def registerUser(user = None):
        from userManagement.repository.UserRepository import UserRepository
        responseBody = bool(UserRepository.saveUser(user))
        return ResponseEntity(body=True)