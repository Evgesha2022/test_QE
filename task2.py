sum_order_=int(input("Введите сумму заказа: "))
dinero_=int(input("Внесённая сумма: "))
def val_change(sum_order, dinero):
    change = dinero - sum_order
    if change==0:
        return "Сдачи нет"
    l_change=[5000, 2000, 1000, 500, 2000, 100, 50, 10, 5, 2 , 1]
    our_change=[0 for i in range(11)]
    ans=""
    for i in range(len(l_change)):
        while(change>=l_change[i]):
            change-=l_change[i]
            our_change[i]+=1
        if our_change[i]!=0:
            ans+=f", {l_change[i]} руб: {our_change[i]} шт."
    ans=ans[2:]
    return ans
print(val_change(sum_order_, dinero_))