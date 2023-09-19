class UserInfo:

    #cls 변수 ( 클래스 변수 == static변수 )

    adminUser = {
        "username" : "root",
        "password" : "1q2w3e4r"
    }

    def __init__(self):
        self.adminUser = {
            "username" : "user1",
            "password" : "1234"
        }

    @classmethod
    def showAdminUser(cls):
        print("[showAdminUser]")
        print(cls.adminUser)



if __name__ == "__main__":
    userInfo = UserInfo()
            # 생성 후 참조문 (소문자작성)
    print(userInfo.adminUser)
            #Static이 이렇게 씀 (대문자로 시작 USerInfo)
    print(UserInfo.adminUser)

    userInfo.showAdminUser()
    UserInfo.showAdminUser()

class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.name = None
        self.email = None

    @staticmethod
    def showUserClassInfo():
        print("그냥 실행 가능한 메소드")


if __name__ == "__main__":
    userInfo = UserInfo()
    print(userInfo.adminUser)
    print(userInfo.adminUser)


    userInfo.showAdminUser()
    UserInfo.showAdminUser()

    User.showUserClassInfo()