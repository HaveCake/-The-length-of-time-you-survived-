# @时间: 2022/12/6 22:01
# @文件: 你幸存的时间长度.py
# @打开工具: PyCharm
coding = "utf-8"

'''
年 = %Y
月 = %m
日 = %d
时 = %H
分 = %M
秒 = %S

'''


def main():
    import time
    当前年 = int(time.strftime('%Y'))
    当前月 = int(time.strftime('%m'))
    当前日 = int(time.strftime('%d'))

    出生年 = int(input("请输入您出生时的年份："))
    出生月 = int(input("请输入您出生时的月份："))
    出生日 = int(input("请输入您出生时的日："))

    # 查看是否是闰年，如果是，返回True，否则返回False
    def leap_year(year_num):
        if year_num % 100 == 0:
            if year_num % 400 == 0:
                return True
            else:
                return False
        else:
            if year_num % 4 == 0:
                return True
            else:
                return False

    print('您已存活：')
    print(当前年 - 出生年, '年')
    print(((当前年 - 出生年) - 1) * 12 + 当前月 + 12 - 出生月, '月')

    天数 = 0
    闰年 = []
    各月天数 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    各月天数_闰 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(当前年 - 出生年 + 1):
        if leap_year(出生年 + i) == True and 出生年 + i != 出生年:
            闰年.append(出生年 + i)

    天数 += ((当前年 - 出生年) - 1 - len(闰年)) * 365 + len(闰年) * 366

    if leap_year(出生年) == True and 出生月 == 2:
        天数 += (29 - 出生日) + 314
    else:
        天数 += (各月天数[出生月] - 出生日) + 314

    if leap_year(当前年) == True and 当前月 > 2:
        for i in range(当前月):
            天数 += 各月天数_闰[i]

    elif leap_year(当前年) == True and 当前月 == 2:
        天数 += 31 + 当前日

    if leap_year(当前年) == False and 当前月 > 2:
        for i in range(当前月):
            天数 += 各月天数[i]

    elif 当前月 == 2:
        天数 += 31 + 当前日



    elif 当前月 == 1:
        天数 += 当前日

    print(天数, '天')
    print(天数 * 24, '小时')
    print(天数 * 24 * 60, '分钟')
    print(天数 * 24 * 60 * 60, '秒')


if __name__ == "__main__":
    main()
