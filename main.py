h=int(input("0 ile 23 arasında bir sayı giriniz: "))


if(1<=h<=23):
    m = int(input("0 ile 59 arasında bir sayı giriniz: "))
    if(h>12):
        convert=(h%12)
        if (0 <= m <= 59):
            if (1 <= m <= 30):
                print("Saat {} {} geçiyor".format(convert, m))
            elif (30 < m <= 59):
                print("Saat {} {} var".format(convert + 1, 60 - m))
        else:
            print("Dakika zaman aralığını dışında")
    else:
        if(0<= m <= 59):
            if(1<=m<=30):
                print("Saat {} {} geçiyor".format(h, m))
            elif(30<m<=59):
                print("Saat {} {} var".format(h+1, 60-m))
        else:
            print("Dakika zaman aralığının dışında")

else:
    print("Saat zaman aralığının dışında")












