# while문 안에서 continue를 만나면 while문의 조건문으로 돌아가 다시 반복문이 실행된다.
# while문 안에서 break을 만나면 while문의 반복문이 종료된다.

# 1. try 와 except를 활용하는 방법
# : 아래는 오류 종류에 상관 없이 오류가 발생하면 except 블록을 수행한다.

try : 
    <수행할 문장1>
except :
    <수행할 문장2>

#   2.  try 와 '발생오류'만 포함한 except문
# : 아래와 같은 경우에는 발생오류와 일치하는 오류가 발생했을 때만 문장2를 수행한다.

try : 
    <수행할 문장1>
except 발생오류 :
    <수행할 문장2>

#     3. 이 경우는 두 번째 경우에서 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법이다.

try:
    ...
except 발생 오류 as 오류 메시지 변수:
    ...

핵심: try 블록 수행 중 오류가 발생하면 except 블록이 수행된다. 하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.

https://wikidocs.net/30

# finally, else 활용 