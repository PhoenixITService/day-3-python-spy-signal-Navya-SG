input=list(map(int,input("enter numbers:").split()))
select=input[1::3]
reverse=select[::-1]
result=[]
for num in reverse:
    result+=chr(num)
print("".join(result))