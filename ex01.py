# 변수의 두개의 값을 서로 바꾸는 예제
from asyncio.base_tasks import _task_print_stack

num1="100"
num2=200
#print(type(num1))
print("num1: ",num1,"num2: ",num2)

# 두개의 변수값을 바꾸기 위해서는 임시변수가 필요하다.
temp=num1
temp=num2
num2=temp

print("num1: ",num1,"num2: ",num2)
