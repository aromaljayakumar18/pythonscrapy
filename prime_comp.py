prime_num=[]
composite_num=[]
for x in range(2, 101):
    count=0
    for j in range(1,x+1):
        if x%j==0:
            count += 1
    if count == 2:
        prime_num.append(x)
    else:
        composite_num.append(x)
print("the prime numbers are: ",prime_num)
print("the composite numbers are: ",composite_num)