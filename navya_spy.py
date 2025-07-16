input=input().split()
input=list(input)
select=input[1::3]
reversed=select[::-1]
result=""
for num in reversed:
    result+=chr(int(num))
print(result)