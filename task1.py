def sum_numbers( x):
    nums = [i for i in range(x + 1)]
    nums[1]=0
    a=2
    while a<=x:
        if nums[a]!=0:
            b=2*a
            while b<=x:
                nums[b]=0
                b+=a
        a+=1
    nums=[i for i in nums if nums[i]!=0]
    ans=0
    print(nums)
    for k in nums:
        ans+=k
    return ans

N=int(input("Введите число: "))
print(sum_numbers(N))

    