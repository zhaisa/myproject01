aa="abc\tdefAAaabbbbbbbcCccccccg"
cc=aa.capitalize()#把字符串的第一个字符大写
print(cc)
dd=aa.center(50)#返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print(dd)
ee=aa.count("b",0,len(aa))#返回 str 在 string 里面出现的次数，
# 如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
print(ee)
ff=aa.encode(encoding="UTF-8",errors="static")#以 encoding 指定的编码格式编码 string，
# 如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
print("编码为：{0}".format(ff))
print(type(ff))
gg=ff.decode(encoding="UTF-8",errors="static")#以 encoding 指定的编码格式解码 string，
# 如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace'
print("解码为：{0}".format(gg))
print(type(gg))
hh=aa.endswith('g',0,len(aa))#检查字符串是否以 obj 结束，如果beg 或者 end
# 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
print(hh)
ii=aa.expandtabs(tabsize=8)#把字符串 string 中的 tab 符号(\t)转为空格，tab 符号默认的空格数是 8。
print(ii)
jj=aa.find('ef',0,len(aa))#检测 str 是否包含在 string 中，
# 如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
print(jj)
kk=aa.format()#格式化字符串
print(kk)
ll=aa.index('ef',0,len(aa))#跟find()方法一样，只不过如果str不在 string中会报一个异常.
print("查找结果为：{0}".format(ll))
mm=aa.isalnum()#如果 string 至少有一个字符并且所有字符都是字母或数字则返
#回 True,否则返回 False
print("至少有一个字符并且所有字符都是字母或数字:{}".format(mm))
nn=aa.isalpha()#如果 string 至少有一个字符并且所有字符都是字母则返回 True,
#否则返回 False
print("至少有一个字符并且所有字符都是字母:{}".format(nn))
oo=aa.isdecimal()#如果 string 只包含十进制数字则返回 True 否则返回 False.
print("只包含十进制数字:{}".format(oo))
pp=aa.isdigit()#如果 string 只包含数字则返回 True 否则返回 False.
print("只包含数字:{}".format(pp))
qq=','.join(aa)#以 string(,) 作为分隔符，将 seq(aa) 中所有的元素(的字符串表示)合并为一个新的字符串
print("{}".format(qq))
print("最大值为：{0}，最小值为：{1},aa的类型为：{2}".format(max(aa),min(aa),type(aa)))
