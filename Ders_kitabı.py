# Ders_kitabm
#Ders kitabını programa ekleyerek istenilen dersi istenilen sayfasını çağırıp ekran da görmek ve daha fazlasını ilerleyen günlerde yapacağım

while True:
    
    print(""" 
    Ders Çalışma Ekranınan Hoş Geldiniz...\n\n
    Ders Listesi Aşağıdaki Gibi

1.)     Türkçe
2.)     Matematik
3.)     Tarih     
""")
    
    Ders_Seç = input("\nİstediğin Ders :")
    
    def türkçe_kitap():
        #Bir txt dosyasından veri cağırdık
        #Çağrılan veriyi bir değişkene eşitledik
        #Eşitlenen değişken aslında bir karakter dizisine 
        #eşitlendiğinden karakterdizilerinin
        #Önce tatmını küçülttük sonrada tamamını büyüttük
        #En son olarak çağrılan metin dosyasını kapadık
        Türkçe_aç = open("turkce_fihrist.txt","r+")
        türkçe_oku = Türkçe_aç.read()
        türkçe_oku = türkçe_oku.lower().swapcase()
        print("\nSeçilen Ders Türkçe\n",türkçe_oku)
        Türkçe_aç.close()
        türkce_kitap_sayfalar()
    
    def türkce_kitap_sayfalar():
        tanım = input ("Gitmek istediğiniz sayfanın numarasını giriniz : ")
        if tanım == "1":
            türkçe_syf1 = open ("turkce_syf1.txt","r+")
            print(türkçe_syf1.read())
            türkçe_syf1.close()

        elif tanım == "2":
            türkçe_syf2 = open ("turkce_syf2.txt","r+")
            print(türkçe_syf2.read())
            türkçe_syf2.close()
                
        elif tanım == "3":
            türkçe_syf3 = open ("turkce_syf3.txt","r+")
            print(türkçe_syf3.read())
            türkçe_syf3.close()
              
    
    
    

    
    if Ders_Seç == "1":
        türkçe_kitap()
    elif Ders_Seç == "2":
        Matematik_aç = open("matematik.docx","r",encoding='Cp1254')
        print("\Seçilen Ders Matematik\n",Matematik_aç.read())
        Matematik_aç.close()
    elif Ders_Seç == "3":
        Tarih_aç = open("tarih.docx","r",encoding='Cp1254')
        print("\Seçilen Ders Tarih\n",Tarih_aç.read())
        Tarih_aç.close()
    
    else:
        print("hata oluştu")
        exit
        
