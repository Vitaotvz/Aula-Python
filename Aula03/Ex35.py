n = int(input("digite o valor de n: "))


while n>100 or n<=0:
    print("O valor deve ser positivo e menor que 100")
    n = int(input("digite n novamente: "))


curr = 2
incr = 3
for i in range(n):
    print(curr)
    curr += incr
    incr += 2
