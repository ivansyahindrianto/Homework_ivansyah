def fibo(n):
    a = 0
    b = 1
    fibo_list = []
    for i in range(n):
        fibo_list.append(a)
        saved = a
        a = b
        b += saved   
    print(fibo_list)