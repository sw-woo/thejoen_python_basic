

# if kor >= 80 :
#     print("합격")
# else:
#     print("불합격")


# student = int(input("몇명의 학생인 가요"))
# student_score = []
# for i in range(student):
#     kor = int(input("국어점수 입력해주세요!"))
#     if kor >= 80:
#         print("A등급")
#         student_score.append("A등급")
#     elif kor >=70 and kor <80:
#         print("B등급")
#         student_score.append("B등급")
#     elif kor >=60 and kor <70:
#         print("C등급")
#         student_score.append("C등급")
#     elif kor >=50 and kor <70:
#         print("D등급")
#         student_score.append("D등급")
#     else :
#         print("F등급")
#         student_score.append("F등급")

# print(student_score)

# file_name = "./fdedd13e73624474d64d04fe1f8e8198/stock1.txt"

# f = open(file_name, "r", encoding="utf-8")
# entire_txt = f.read()
# print(entire_txt)
# f.close()

# num = 1

# while num <= 100:
#     if num % 2 ==0:
#         print(num)
#     num +=1


# count = 1
# distance = 12.5
# total_distance = 0

# while count <=10 :
#     total_distance += distance
#     # total_distance = total_distance+distance
#     print(f"{count}번째 거리는 {total_distance}km입니다.")
#     count += 1

# print(f"전체 달린 거리는: {total_distance}")

# math = int(input("수학 점수 입력하세요"))

# kor = int(input("국어 점수 입력하세요"))

# eng = int(input("영어 점수 입력하세요"))

# total = math+kor+eng
# avg = total/3

# if avg >= 80:
#     print("합격")
#     print(f"평균은: {avg}")
# if avg ==60:
#     print("운이 좋았다.")
#     print(f"평균은: {avg}")

# if kor >=80 and eng>=60 :
#     print("합격")
#     print(f"평균은: {avg}")

# japan_city_famous =["오사카","삿포르","후쿠오카"]
# user_input= []
# status = True

# while status :
#     print("일본의 3개 유명 관광명소를 작성해주세요!")
#     user_input.clear() # 이전입력값 전체 삭제
#     for i in range(len(japan_city_famous)):
#         japan_city = input(f"{i+1}번째 유명한 일본 관광지를 입력하세요: ")
#         user_input.append(japan_city)
    
#     if set(user_input) == set(japan_city_famous):
#         print("축하합니다! 정답입니다!")
#         status = False
#     else:
#         print("다시 작성해주세요! 입력한 관광지가 일치하지 않거나 중복된 관광지가 있을 수 있습니다.")




# file_name = "./stock_practice/stock1.txt"
# f = open(file_name, "r", encoding="utf-8")
# entire_txt = f.read()
# print(entire_txt)
# f.close()


dic = {'이름':"우성우","job":"직장인 개발자"}
print(dic)
print(dic['이름']+' is '+dic['job'])
print(f"{dic['이름']} is {dic['job']}")
















