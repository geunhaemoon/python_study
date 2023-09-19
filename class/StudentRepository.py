class StudentRespository:

    def __init__(self):
        self.studentList = []
        #self.studentList = list{} 같음

    def add(self, student):
        self.studentList.append(student)
        print("학생을 추가하였습니다.")

    def findStudentByName(self, name):
        for student in self.studentList:
            if student.name == name:
                return student
        return None

def main():
    from Student import Student
    # form: 모듈 파일 import : 모듈 내부의 클래스, 함수, 변수
    sr = StudentRespository()
    sr.add(Student("문근해", 25))
    sr.add(Student("문근달", 26))
    sr.add(Student("문근별", 27))
    sr.add(Student("문근바다", 28))

    print(sr.studentList)

    print(sr.findStudentByName("문근해"))


if __name__ == "__main__":
    main()

print("학생저장소모듈", __name__)