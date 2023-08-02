N=int(input("Введите количество циклопов: "))
arr_=[]
for i in range(N):
    arr_.append(int(input()))
def pars(n, arr_raw):
    ans=[]
    arr=sorted(arr_raw)
    k=0
    min=0
    new_arr=[0, 0, 0]
    for i in range(len(arr)):
        if min!=None: 
            min=arr[i]-1
        sr=arr[i]
        max=arr[i]+1
        new_arr[0]=arr[i-1]-1
        new_arr[1]=arr[i-1]
        new_arr[2]=arr[i-1]+1
        min_count=new_arr.count(min)
        
        
        if min_count!=0 :
            min=None
            continue
        k+=2
        min=0
    if k<len(arr):
        k+=2
    return int(k/2)


print(pars(N, arr_))