#	객체를 파일로 저장하고 불러오기		pickle
import pickle


def get_all_data():
    try:
        with open("data.p", 'rb') as f: 
            return pickle.load(f)
    except FileNotFoundError:
        return {}


def add_data(no, subject, content):
    data = get_all_data()
    assert no not in data
    data[no] = {'no': no, 'subject': subject, 'content': content}
    with open('data.p', 'wb') as f:
        pickle.dump(data, f)


def get_data(no):
    data = get_all_data()
    return data[no]


# 데이터저장
add_data(1, '안녕 피클', '피클은 매우 간단합니다.')

# 데이터조회
data = get_data(1)
print(data['no'])
print(data['subject'])
print(data['content'])


#	객체 변경에 따른 오류를 방지하려면? ― copyreg
import pickle
import copyreg


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def pickle_student(student):
    kwargs = student.__dict__
    return unpickle_student, (kwargs, )


def unpickle_student(kwargs):
    return Student(**kwargs)


copyreg.pickle(Student, pickle_student)

a = Student('임철희', 27)
with open('student.p', 'wb') as f:
    pickle.dump(a, f)


#	딕셔너리를 파일로 저장하려면? ― shelve
import shelve


def save(key, value):
    with shelve.open('shelve.dat') as d:
        d[key] = value


def get(key):
    with shelve.open('shelve.dat') as d:
        return d[key]


save('number', [1, 2, 3, 4, 5])
print(get('number'))  # [1, 2, 3, ,4, 5] 출력

"""
pickle과 shelve의 차이
pickle : 모든 객체 처리 가능
shelve : 딕셔너리 객체만 처리 가능
"""