print(""" 1- Toplama
2 - Çıkarma
3- Çarpma
4 - Bölme
5 - Çıkış
""")


a = input("Birinci sayıyı giriniz :")
a = int(a)
b = input("İkinci sayıyı giriniz :")
b = int(b)

secim = input("Hangi işlemi yapmak istiyorsunuz ? : ( 1, 2, 3, 4, 5) ")

match secim:
    case "1":
        sonuc  = a+b
        print(sonuc)
    case "2":
        sonuc = a - b
        print(sonuc)
    case "3":
        sonuc = a * b
        print(sonuc)
    case "4":
        sonuc = a // b
        print(sonuc)
    case "5":
        pass
    case _:
        print(" Yanlış seçim yaptınız.")