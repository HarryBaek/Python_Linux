a = 10
b = 1 
# b값 : 0을 넣으면 except 실행
# b값 : 1을 넣으면 except 미실행하고 바로 c 출력

try : 
    c = a / b

except ZeroDivisionError:
    c = 5

print(c)


# 예외처리
# try :
#   c = a / b
# except:
#     pass
