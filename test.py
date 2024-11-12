# 문자열
# num = "안녕하세요\n"
# print(num*5)

# str = "power"
# # print(len(str))
# print(str[0]+str[2]+str[4])
# print(str[0:3])

# str = input("입력하세요 : ")
# print(str)

# num = int(input("입력하세요 : "))
# print(num)

num1, num2 = map(int,input("숫자 입력 2개 : ").split())
# re = int(num1) * int(num2)
# print("결과 =" , re)
print(num1+num2)


# num1,num2 = int(input("입력하세요 : ").split())
# num1 = 10
# num2 = 20
# if num == 1:
#     print(num1+num2)
# else:
#     exit()

# while True:
#     score = int(input("입력하세요 : "))
    
#     if score >=90:
#         print("A")    
#     elif score >=80:
#         print("B")
#     elif score >=70:
#         print("C")
#     elif score >=60:
#         print("D")
#     else:
#         print("낙제 프로그램 종료")
#         # exit()
#         break
  

#list
# str1 = [1,2,3,4,5]
# str2 = ["a","b","c"]
# print(str1)
# print(str2)
# str2.append(6)
# str1.insert(2,0)
# print(str1)
# str1.remove(3)
# print(str1)




#for//while 반복문
# num = [1,2,3,4,5]
# for i in range(5):
#     if num[i] % 2 == 0:
#         print(num[i])

# num = [5,15,12,30,17]
# for i in range(5):
#     if num[i] % 3 == 0 or num[i]%5==0:
#         print(num[i])


# 2중 for문
for i in range(5):
    for j in range(i):
        print("*", end="")
    print()