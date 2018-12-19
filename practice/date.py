import datetime
import time
if __name__ =='__main__':
    d=datetime.date.today().strftime('%y-%m-%d %H-%M-%S')
    print("这是第一行:"+d)#18-11-29 00-00-00
    print("这是第二行:"+str(time.time()))
    d=datetime.time()#00:00:00
    print("这是第三行："+str(d))
    d=datetime.date(2021,1,1)#2021-01-01
    print("这是第四行：" + str(d))
    d=d +datetime.timedelta(days=10)
    print("这是第五行：" + str(d))

