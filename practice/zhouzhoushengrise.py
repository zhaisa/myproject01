def zzsrate(money,days,myrate):

    # input("请输入金额：")
    # input("请输入持有天数：")
    # nowrate=input("请输入目前利率：")
    firstzqrate=rate=myrate
    factrate=rate/100
    print("持有周数为：{}".format(days//7+1))
    zq=(days-8)//7+1
    nowrate=firstzqrate+(zq-1)/10
    if days%7!=0:
        factdays=days+(7-days%7)
    else:
        factdays=days

    for i in range(1,zq+1):
        nowrate = (firstzqrate + (i - 1) / 10)/100
        nowrate=round(nowrate,3)
        print("本周期的利率为{}".format(nowrate))
        daymoney = money * (nowrate / 365)
        factmoney = round(daymoney,2) + 0.01
        print("本周期每日利息为{}".format(factmoney))
        if i==1 :
            summoney1=daymoney*8
        else:

            summoney2 = summoney1+daymoney*i*7
            if days%7==0:
                summoney3=summoney2
            else:
                summoney3=summoney2+(7-days%7)*daymoney


    print(money,"的基础利息为：%.2f"%summoney3)
    return summoney3

zzsrate(100,180,5.0)