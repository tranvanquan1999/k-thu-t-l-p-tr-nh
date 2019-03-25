for num in range(0,10):
    for i in range(2,num):
        if num%i == 0:
            j=num/i
            print('%d bằng %d * %d' %(num,i,j))
            break
        else:
            print(num,'là số nguyên tố')