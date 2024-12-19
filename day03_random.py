# import random

# def generate_student(num_trials:int, student_list:list):
#     """학생들을 랜덤하게 선택하여 리스트를 반환하는 함수"""
#     return [random.choice(student_list) for _ in range(num_trials)]

# def count_students(student, random_student):
#     """랜덤하게 선택된 학생들의 빈도수를 카운트하는 함수"""
#     student_count = {name:0 for name in student}

#     for name in random_student:
#         student_count[name] +=1

#     return student_count

# def find_most_selected(student_count:dict):
#     """빈도수가 가장 높은 학생을 찾는 함수"""
#     return max(student_count, key = student_count.get)

# def play_selection_game(student:list):
#     """선택 게임을 실행하는 함수"""
#     # student = ["성우","민수","미선","세완","형록","수빈"]
#     # num_student = int(input("몇명의 학생이 있는가요?:"))
#     # student = [input(f"학생{i+1}의 이름을 입력하세요")for i in range(num_student)]
#     num_trials = int(input("몇번의 랜덤 선택을 진행 할까요?:"))
#     random_student = generate_student(num_trials, student)
#     student_count = count_students(student, random_student)
#     return find_most_selected(student_count), student_count

# # if __name__ == "__main__":
# #      print(play_selection_game())

    














# # student = ["성우","민수","미선","세완","형록","수빈"]

# # num = 0
# # random_student = []
# # while num <10:
# #     random_student.append(random.choice(student))
# #     num +=1

# # random_student_count = {name:0 for name in student}

# # for name in random_student:
# #     random_student_count[name] +=1


# # print(random_student)
# # print(random_student_count)

# # #가장 많이 선택된 사람 찾기 
# # most_selected = max(random_student_count, key=random_student_count.get)
# # print(f"{most_selected}가 가장 많이 선택되었습니다.")
