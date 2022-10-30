
import random

def musteri_ekle():
    adet = int(input("Kaç Müşteri Kaydı Eklenecek?: "))
    for i in range(adet):
        with open("otomasyon.txt", "r", encoding="utf-8") as file:
            liste = file.readlines()
        dogru = 1
        while dogru:
            sira_no = random.randint(500,10000)  # her müşteri için random sıra numaraları oluşturuldu.
            kume = set()  # boş küme oluşturuldu
            kume.add(str(sira_no))
            for j in liste:
                j = j.split(":")  # sıra numarası bulunan satır boşluklara göre split ile elemanların ayrıldı.
                kume.add(j[1].split(" ")[1])
                # split ile ayrılan listenin ilk 1. elemanında sıra numarası olduğu için bu eleman dasplit ile başka bir liste haline getirildi.
                # en son oluşan listenin ilk elemanı olan sıra numarası alınıp kümeye eklendi
            if len(liste) != len(kume):# küme sayesinde eleman sayıları karşılaştırıldı
                dogru = 0

        print("{}. Müşterinin: ".format(i + 1))
        ad = input("Adı: ")
        soyad = input("Soyadı: ")
        telno = input("Telefon Numarası:")

        def abonmandurumu():
            try:
                while True:
                    abonman = int(input("Aylık Abonman Yaptırma Durumu (Var-> 1, Yok->2):"))
                    if abonman == 1:
                        abonman_durum = "Var"
                    elif abonman == 2:
                        abonman_durum = "Yok"
                    else:
                        print("Yanlış Tuşlama Yaptınız!")
                        continue
                    return abonman_durum
            except ValueError:
                print("Yanlış bilgi girdiniz!")

        durum = abonmandurumu()


        if durum == "Yok":
            while True:
                giris_saati = float(input("Araç Giriş Saati(Lütfen saati (xx.00) şeklinde tam saat giriniz): "))
                cikis_saati = float(input("Araç Çıkış Saati(Lütfen saati (xx.00) şeklinde tam saat giriniz): "))
                if cikis_saati < giris_saati:
                    print("Çıkış Saati Giriş Saatinden Küçük Olamaz!")
                    continue
                else:
                    break

            with open("otomasyon.txt", "a", encoding="utf-8") as dosya:
                dosya.write("Sıra Numarası: " + str(sira_no) + " Ad: " + ad + " Soyad: " + soyad + " Telefon Numarası: " + telno + " Abonman Durumu: " + durum + " Giriş Saati: " + str(
                    giris_saati) + " Çıkış Saati: " + str(cikis_saati))
                dosya.write("\n")

        elif durum == "Var":
            with open("otomasyon.txt", "a", encoding="utf-8") as dosya:
                dosya.write("Sıra Numarası: " + str(
                    sira_no) + " Ad: " + ad + " Soyad: " + soyad + " Telefon Numarası: " + telno + " Abonman Durumu: " + durum)
                dosya.write("\n")



        print("Müşteri Kaydı Eklendi.")


def musteri_ara():
    with open("otomasyon.txt", "r", encoding="utf-8") as file:
            liste = file.readlines()

    def icfonk():
        nonlocal liste # bir üst fonksiyondaki listeyi kullanabilmek için nonlocal kullanıldı
        print("-------------------------------------------")

        print("Tüm Müşteriler: ")
        for a in liste:
            print(a)
        print("-------------------------------------------")


    icfonk()
    aranan = input("Listelenen Müşterilerden Aranan Müşterinin Sıra Numarası: ")
    for i in liste:
        if aranan in i:
                print(i)

def guncelle():

    with open("otomasyon.txt", "r+", encoding="utf-8") as dosya:
        liste = dosya.readlines()

        def icfonk():
            nonlocal liste
            print("-------------------------------------------")

            print("Tüm Müşteriler: ")
            for a in liste:
                print(a)
            print("-------------------------------------------")

        icfonk()
        kim = input("Listelenen Müşterilerden Çıkış Saati Güncellenecek Olan Müşterinin Sıra Numarası: ")
        for i in liste:
            if kim in i:
                satir = i
                bol = satir.split()
                durum = bol[-7]
                # listedeki sıra numarası aranan kişinin olduğu satır splitle ayrı bir liste olarak oluşturuldu ve ulaşıldı

                if durum == "Yok":
                    for i in liste:
                        if kim in i:
                            newlist = liste.copy()  # liste kopyalanarak kopya liste üzerinden işlem yapıldı.
                            liste.remove(i)
                    guncel = input("Yeni Çıkış Saati(Giriş Saatinden Büyük Bir Değer Giriniz): ")

                    for i in newlist:
                        if kim in i:
                            satir = i
                            bol = satir.split()  # listenin elemanı alınarak içindeki bilgiler split metodu ile listeye dönüştürüldü

                            bol[-1] = guncel  # split ile oluşturulan listenin en sondaki elemanı alındı ve değiştirildi

                            son = " ".join(bol)  # değiştirilmiş haliyle split ile ayrılan liste tekrar birleştirildi
                            newlist.remove(i)  # kopya listedeki güncellenmemiş satır silindi
                            print("\n")
                            newlist.append(son)  # kopya listeye join ile birleştirilen yeni karakter dizisi eklendi.
                    with open("otomasyon.txt", "w", encoding="utf-8") as dosya:
                        dosya.writelines(newlist)
                else:

                    print("Müşterinin Aylık Abonmanı Bulunduğu İçin Çıkış Saati Kayıt Alınmamıştır Ve Dolayısıyla güncellenemez.")


def kayit_sil():
    with open("otomasyon.txt", "r", encoding="utf-8") as file:
        liste = file.readlines()

        def icfonk():
            nonlocal liste
            print("-------------------------------------------")

            print("Tüm Müşteriler: ")
            for a in liste:
                print(a)
            print("-------------------------------------------")

        icfonk()
    with open("otomasyon.txt", "w", encoding="utf-8") as file:
        silinecek =input("Listelenen Müşterilerden Kaydı Silinecek Müşterinin Sıra Numarası: ")
        for i in liste:
            if silinecek in i:
                liste.remove(i)
                file.writelines(liste)
        print("Kayıt Başarıyla silindi")

def musteri_listele():
    with open("otomasyon.txt","r",encoding="utf-8") as dosya:
        print("Tüm Müşterilerin Bilgileri:\n")
        print("---------------------")
        for i in dosya:
            print(i , end="")

def borc_hesapla():

    with open("otomasyon.txt", "r", encoding="utf-8") as dosya:
        liste = dosya.readlines()
    def icfonk():
        nonlocal liste
        print("-------------------------------------------")

        print("Tüm Müşteriler: ")
        for a in liste:
            print(a)
        print("-------------------------------------------")

    icfonk()
    sira = input("Listelenen Müşterilerden Borcu Hesaplanacak Müşterinin Sıra Numarası: ")
    for i in liste:
        if sira in i:
            satir = i
            bol = satir.split()
            durum = bol[-7]
            if durum == "Yok" : # abonaman durumu yoksa bu if bloğuna girer ve saate göre borç hesaplar

                kampanyalar = {'4_saat': 45, '5_saat': 55, '6_saat': 65, '7_saat': 75, '8_saat': 85, 'tum_gun': 90}
                for i in liste:
                    if sira in i:
                        satir = i
                        bol = satir.split()  # Listede hesap yapılacak satır split ile ayrılarak yeni bir listeye dönüştürüldü.
                        kalinan_saat = float(bol[-1]) - float(bol[-4])
                        # split le ayrılan satırın elemanları olan çıkış saatinden giriş saati çıkarılarak aracın otoparkta kaldığı süre bulundu.
                        if kalinan_saat == 4:
                            borc = kampanyalar['4_saat']
                        elif kalinan_saat == 5:
                            borc = kampanyalar['5_saat']
                        elif kalinan_saat == 6:
                            borc = kampanyalar['6_saat']
                        elif kalinan_saat == 7:
                            borc = kampanyalar['7_saat']
                        elif kalinan_saat == 8:
                            borc = kampanyalar['8_saat']
                        elif kalinan_saat >= 9:
                            borc = kampanyalar['tum_gun']
                        else:
                            borc = kalinan_saat * 12

                        print("Araç Borcu {} Tl'dir.".format(borc))

            else:

                abonmanode()
def abonmanode():
    print("Bilgilendirme!")
    print("------------------")
    print("Aylık Abonman Ücreti Tek Araç İçin 30 Günlük 1800 TL'dir.")
    print("------------------\n")


    while True:
        iptal = int(input("Abonmanınızı iptal etmek için 1'e Aylık Abonman Hesabı İçin 0'a basınız.\n"))

        if iptal == 1:
            def abonmaniptal():
                devam = int(input("Abonman İptal Ettikten Sonra Kaldığınız Gün Sayısı Kadar Tüm Gün Kampanyası Miktarında Borç Ödemeniz Gerekir."
                                  "\nUYARI: Abonman İptali Yaparsanız Kaydınız Silinecek ve Tekrar Kayıt Yaptırmanız Gerekecektir! "
                                  "\nHala Devam Etmek İstiyorsanız 1'i Tuşlayınız. İşlem İptali İçin bir rakam Tuşlayınız: "))

                if devam == 1:

                    kacgun = int(input("Abonmanınızı Kaç Gün Kullandınız?: "))
                    borc = 90 * kacgun
                    print("Abonman İptali Sonrası Araç Borcu {} TL'dir.".format(borc))
                    with open("otomasyon.txt", "r", encoding="utf-8") as dosya:
                        liste = dosya.readlines()

                        def icfonk():
                            nonlocal liste
                            print("-------------------------------------------")
                            print("Tüm Müşteriler: ")
                            for a in liste:
                                print(a)
                            print("-------------------------------------------")

                        icfonk()

                    with open("otomasyon.txt", "w", encoding="utf-8") as file:
                        sira = input("\nAbonman İptali İçin Tekrar Aynı Müşteri Sıra Numarasını Gİrin:  ")
                        for i in liste:
                            if sira in i:
                                liste.remove(i)
                                file.writelines(liste)
                    print("\nAbonman İptali Sonucu Borç Hesaplandı Ve Kayıt Silindi.")

                else:
                    print("İşlem İptal Edildi.")

            abonmaniptal()
            break
        elif iptal == 0:
            print("Aracınız için Toplam Borç Tutarı: 1800 TL'dir.")
            break
        else:
            print("Yanlış Tuşlama Yaptınız!")
            continue



def ana_fonksiyon():
    while True:
        print("\n"
              "--------------------------------------")
        print("\t\t OTOPARK OTOMASYONU \t\t ")
        print("--------------------------------------")
        print("(1)- Müşteri Ekleme")
        print("(2)- Müşteri Arama")
        print("(3)- Müşteri Çıkış Saati Güncelleme")
        print("(4)- Müşteri Kaydı Silme")
        print("(5)- Müşterileri listeleme")
        print("(6)- Müşteri Borcu Hesaplama")
        print("(7)- Aylık Abonman Ödeme ")
        print("(0)- Çıkış")
        print("--------------------------------------")

        secim = int(input("Yapmak istediğiniz İşlemi Seçiniz: "))
        print("--------------------------------------")
        if secim == 1:
            musteri_ekle()
        elif secim == 2:
            musteri_ara()
        elif secim == 3:
            guncelle()
        elif secim == 4:
            kayit_sil()
        elif secim == 5:
            musteri_listele()
        elif secim == 6:
            borc_hesapla()
        elif secim == 7:
            abonmanode()
        elif secim == 0:
            print("OTOMASYONDAN ÇIKIŞ YAPILIYOR...")
            break
        else:
            print("Hatalı Seçim Yaptınız!")
ana_fonksiyon()






