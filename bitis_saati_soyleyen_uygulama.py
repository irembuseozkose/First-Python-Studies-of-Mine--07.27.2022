hour = int(input("Başlayış saatinin saat kısmını giriniz: "))
mins = int(input("Başlayış saatinin dakika kısmını giriniz: "))
dura = int(input("Olayın kaç dakika süreceğini giriniz: "))

zaman= hour*60+mins #
toplamdakika=zaman+dura
print(toplamdakika//60,".",toplamdakika%60,"da süre bitecektir.")
#BuseOzkose 7/27/2022
