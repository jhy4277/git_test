# 한사람이 돈이 5000원이 있는데 사탕의 가격이 120원이라면 최대로 살 수 있는 사탕의 수는 몇개인지 알아보는 프로그램

mymoney=5000
candyprice=120
#최대로 살 수 있는 사탕의 개수
numcandies=mymoney//candyprice
# /를 하나로 넣으면 실수, // 적용하면 정수로 결과값이 나온다.
print("최대로 살 수 있는 사탕의 개수:",numcandies)

#최대로 살 수 있는 사탕을 구입하고 남은 돈
change= mymoney%candyprice
print("남은돈:",change)