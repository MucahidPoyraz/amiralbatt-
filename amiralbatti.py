


import random

# boş listelerimiz yazdık
liste = []
liste1 = []
liste2 = []
liste3 = []
liste4 = []
listeatıs = []

# oyun haritası belirleniyor ve gemiler rasgele olacak şekilde yerleştiriliyor
def play():
    # oyun haritası en az 10x10 olması gerekiyor kontrol yapılıyor
    while 1 == 1:
        bolge = int(input("HxH karesel haritanın bir kenarını giriniz(en az 10 olacak şekilde) >"))
        if bolge < 10:
            print("en az 10 olacak şekilde giriniz")
        else:
            break
    # 1 birimlik gemi oyun alanında rasgele bir yere yerleşiyor
    baslangıc = random.randrange(1, bolge * bolge + 1)
    liste1.append(baslangıc)
    # 2 birimlik gemi için yönü belirleniyor ve buna göre haritada uygun yere yerleştirliyor
    yön = random.randrange(0, 2)
    if yön == 0:
        kontrol = 0
        while kontrol < bolge:
            kontrol = 0
            baslangıc = random.randrange(1, bolge * bolge)
            # baslangıc nok. uygunlugu kontrol ediliyor
            for x in range(bolge):
                if baslangıc % bolge != 0:
                    kontrol += 1
                else:
                    break
                # eger geminin herhangi bir parçası başka gemiler ile çakıırsa yeni başlangıc nok. belirlenecek
                if baslangıc + x in liste1:
                    break
        # geminin parçaları listeye ekleniyor
        liste2.append(baslangıc)
        liste2.append(baslangıc + 1)

    else:
        kontrol = 0
        while kontrol < 1:
            kontrol = 0
            baslangıc = random.randrange(1, (bolge - 1) * (bolge - 1))
            for x in range(2):
                # eger geminin herhangi bir parçası başka gemiler ile çakıırsa yeni başlangıc nok. belirlenecek
                if baslangıc + bolge * x in liste1:
                    break
                else:
                    kontrol += 1
        # geminin parçaları listeye ekleniyor
        liste2.append(baslangıc)
        liste2.append(baslangıc + bolge)
    # 3 birimlik gemi için yönü belirleniyor ve buna göre haritada uygun yere yerleştirliyor
    yön = random.randrange(0, 2)
    if yön == 0:
        kontrol = 0
        while kontrol < bolge:
            kontrol = 0
            baslangıc = random.randrange(1, bolge * bolge)
            # baslangıc nok. uygunlugu kontrol ediliyor
            for x in range(bolge):
                if baslangıc % bolge < (bolge - 1) and baslangıc % bolge != 0:
                    kontrol += 1
                else:
                    break
                # eger geminin herhangi bir parçası başka gemiler ile çakıırsa yeni başlangıc nok. belirlenecek
                if baslangıc + x in liste1 or baslangıc + x in liste2:
                    break
        # geminin parçaları listeye ekleniyor
        liste3.append(baslangıc)
        liste3.append(baslangıc + 1)
        liste3.append(baslangıc + 2)

    else:
        kontrol = 0
        while kontrol < 3:
            kontrol = 0
            baslangıc = random.randrange(1, (bolge - 2) * (bolge - 2))
            for x in range(3):
                # eger geminin herhangi bir parçası başka gemiler ile çakıırsa yeni başlangıc nok. belirlenecek
                if baslangıc + bolge * x in liste1 or baslangıc + bolge * x in liste2:
                    break
                else:
                    kontrol += 1
        # geminin parçaları listeye ekleniyor
        liste3.append(baslangıc)
        liste3.append(baslangıc + bolge)
        liste3.append(baslangıc + bolge * 2)
    # 4 birimlik gemi için yönü belirleniyor ve buna göre haritada uygun yere yerleştirliyor
    yön = random.randrange(0, 2)
    if yön == 0:
        kontrol = 0
        while kontrol < bolge:
            kontrol = 0
            baslangıc = random.randrange(1, bolge * bolge)
            # baslangıc nok. uygunlugu kontrol ediliyor
            for x in range(bolge):
                if baslangıc % bolge < (bolge - 2) and baslangıc % bolge != 0:
                    kontrol += 1
                else:
                    break
                # eger geminin herhangi bir parçası başka gemiler ile çakıırsa yeni başlangıc nok. belirlenecek
                if baslangıc + x in liste1 or baslangıc + x in liste2 or baslangıc + x in liste3:
                    break
        # geminin parçaları listeye ekleniyor
        liste4.append(baslangıc)
        liste4.append(baslangıc + 1)
        liste4.append(baslangıc + 2)
        liste4.append(baslangıc + 3)

    else:
        kontrol = 0
        while kontrol < 4:
            kontrol = 0
            baslangıc = random.randrange(1, (bolge - 2) * (bolge - 2))
            for x in range(3):
                # eger geminin herhangi bir parçası başka gemiler ile çakıırsa yeni başlangıc nok. belirlenecek
                if baslangıc + bolge * x in liste1 or baslangıc + bolge * x in liste2 or baslangıc + bolge * x in liste3:
                    break
                else:
                    kontrol += 1
        # geminin parçaları listeye ekleniyor
        liste4.append(baslangıc)
        liste4.append(baslangıc + bolge)
        liste4.append(baslangıc + bolge * 2)
        liste4.append(baslangıc + bolge * 3)
    # bütün gemi listeleri tek bir liste ye eşitliyorum bu daha sonra işime arayacak
    liste = liste1 + liste2 + liste3 + liste4
    menu(bolge, liste)


def menu(bolge, liste):
    bolge = bolge
    liste = liste
    tercih = "e"
    # gemiler haritada uygun alanlara yerleştirkten sonra oyun menümüz açılıyor
    while (tercih == "e"):

        print("\n")
        print('\t', '\t', "MENÜ")
        print('\t', "[1] gizli modda aç")
        print('\t', "[2] açık modda aç")
        print('\t', "[3] çıkış")

        secim = int(input("seciminizi giriniz >"))
        print("\n")

        if secim == 1:
            for sutun in range(bolge):
                for satir in range(bolge):
                    print("?", '\t', end=" ")
                print("\n")
            print("\n")

            game(bolge, secim, liste)

        elif secim == 2:
            sayac = 1
            for sutun in range(bolge):
                for satir in range(bolge):
                    if sayac in liste:
                        print("#", '\t', end=" ")
                    else:
                        print("?", '\t', end=" ")
                    sayac += 1
                print("\n")

            game(bolge, secim, liste)

        elif secim == 3:
            print("çıkış yaptınız")

        else:
            print("yanlış seçim yaptınız tekrar  deneyiniz")

        tercih = input("tekrar oynamak istermisin <E>vet yada <H>ayır? >: ").lower()


def game(bolge, secim, liste):
    bolge = bolge
    secim = secim
    liste = liste
    hak = 0
    isabet = 0
    # oyuncu bütün gemileri vurdugunda yada hakkı bittiginde oyun sonlanacak
    while 1 == 1:
        if hak < bolge * bolge / 3 and isabet < 10:

            # oyuncu haritanın dışında veya daha önce atış yapmış oldugu kareye atış yapamaz
            while 1 == 1:
                while 1 == 1:
                    print(1, "ile", bolge * bolge, "arasında bir sayi giriniz >", end="")
                    atıs = int(input())
                    if atıs > 0 and atıs <= bolge * bolge:
                        break
                    else:
                        print("lütfen uygun alana atış yapınız")
                if atıs in listeatıs:
                    print("zaten buraya atış yaptınız")
                else:
                    # her uygun atış listeatıs a ekleniyor daha sonra bu listeden faydalanacagım
                    listeatıs.append(atıs)
                    break
                    # atış yapılan bölgenin bir gemiye hasar verip vermedigi kontrol ediliyor
            if atıs in liste:
                print("tebrikler bir gemiye hasar verdiniz")
                isabet += 1
                # bir gemiyi batırıp batırmadıgı kontrol ediliyor
                kontrol = 0
                for x in listeatıs:
                    if x in liste1:
                        kontrol += 1
                    if kontrol == 1:
                        liste1.clear()
                        print("tebrikler bir gemiyi batırdınız")
                        break

                kontrol = 0
                for x in listeatıs:
                    if x in liste2:
                        kontrol += 1
                    if kontrol == 2:
                        liste2.clear()
                        print("tebrikler bir gemiyi batırdınız")
                        break
                kontrol = 0
                for x in listeatıs:
                    if x in liste3:
                        kontrol += 1
                    if kontrol == 3:
                        liste3.clear()
                        print("tebrikler bir gemiyi batırdınız")
                        break

                kontrol = 0
                for x in listeatıs:
                    if x in liste4:
                        kontrol += 1
                    if kontrol == 4:
                        liste4.clear()
                        print("tebrikler bir gemiyi batırdınız")
                        break

                harita(secim, bolge, liste, listeatıs)

            else:
                # karavana atışlar da haritada gösteriliyor ve yalnızca karavana atışlardan oyuncu puan kaybeder
                print("karavana atış yaptınız")
                harita(secim, bolge, liste, listeatıs)
                hak += 1
        elif isabet==10:
            print("TEBRİKLER!!! BÜTÜN GEMİLERİ BATIRARAK OYUNU KAZANDINIZ")
            puan = int(bolge * bolge / 3) - int(hak)
            print("PUANINIZ : ", puan)
            listeatıs.clear()
            break
        else:
            print("OYUN BİTTİ KAYBETTİNİZ")
            puan = 0
            print("PUANINIZ : ", puan)
            listeatıs.clear()
            break


def harita(secim, bolge, liste, listeatıs):
    bolge = bolge
    secim = secim
    liste = liste
    listeatıs = listeatıs
    sayac = 1
    # her uygun atıştan sonra oyun haritası tazeleniyor
    if secim == 1:
        print("\n")
        for x in range(bolge):
            for y in range(bolge):
                if sayac in listeatıs:
                    if sayac in liste:
                        print("x", '\t', end=" ")
                    else:
                        print("*", '\t', end=" ")
                else:
                    print("?", '\t', end=" ")
                sayac += 1
            print("\n")

    if secim == 2:
        print("\n")
        for x in range(bolge):
            for y in range(bolge):
                if sayac in listeatıs:
                    if sayac in liste:
                        print("x", '\t', end=" ")
                    else:
                        print("*", '\t', end=" ")
                elif sayac in liste:
                    print("#", '\t', end=" ")
                else:
                    print("?", '\t', end=" ")
                sayac += 1
            print("\n")
play()