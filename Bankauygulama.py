from os import system as komut
import time


class Muster():
    def __init__(self, AD, ID, PAROLA):
        self.isim = AD
        self.id = ID
        self.parola = PAROLA
        self.bakiye = 0


class Banka():
    def __init__(self):
        self.musteriler = list()

    def muster_ol(self, AD:str, ID:str, PAROLA:str):
        self.musteriler.append(Muster(AD, ID, PAROLA))
        print("Bankamıza kayıt yaptığınız için teşekkürler!")
        print("Ana menüye yönlendiriliyorsunuz...")
        time.sleep(5)



def gec():
    print("Ana menüye yönlendiriliyorsunuz...")
    time.sleep(3)

def gec2():
    print("Menüye yönlendiriliyorsunuz...")
    time.sleep(3)

def gec3():
    print("Menüye yönlendiriliyorsunuz...")
    time.sleep(5)


def main():
    banka = Banka()
    while True:
        komut("cls")
        print("""           |KERO Banka Hoş Geldiniz|
        [1] Banka Müşterisiyim
        [2] Banka Müşterisi Olmak İstiyorum
        [Q] Çıkış İçin!
        """)
        secim = input("Seçiminiz: ")

        if secim == "1":
            ids = [i.id for i in banka.musteriler]
            ID = input("ID: ")
            if ID in ids:
                for Muster in banka.musteriler:
                    if ID == Muster.id:
                        print("|Hoş Geldin {}|".format(Muster.isim))
                        parola = input("Parolanız: ")
                        if parola == Muster.parola:
                            print("Giriş Başarılı!")
                            print("Menüye Yönlendiriliyorsunuz...")
                            time.sleep(3)
                            while True:
                                komut("cls")
                                print("""
        [1] Bakiye Sorgula
        [2] Para Yatır (Kendi Hesabıma)
        [3] Para Yatır (Başkasının Hesabına)
        [4] Para Çek
        [Q] Çıkış""")

                                sec2 = input("işleminiz: ")
                                if sec2 == "1":
                                    print("Bakiyeniz = {} TL".format(Muster.bakiye))
                                    gec2()


                                elif sec2 == "2":
                                    miktar = int(input("Miktar: "))
                                    onay = input("""Kendi hesabınıza {} TL para yatırma işlemini 
                                    onaylıyor musunuz? E/H\n""".format(miktar))
                                    if onay == "E" or onay == "e":
                                        Muster.bakiye += miktar
                                        print("Paranız Yatırıldı!")
                                        gec2()
                                    elif onay == "H" or onay == "h":
                                        print("İşlem İptal Edildi!")
                                        gec2()
                                    else:
                                        print("Hatalı Girildi, İşlem İptal Edildi!")
                                        gec2()


                                elif sec2 == "3":
                                    arananID = input("Musteri ID: ")
                                    if arananID in ids:
                                        for digermusteri in banka.musteriler:
                                            if arananID == digermusteri.id:
                                                miktar = int(input("Miktar: "))
                                                if miktar <= Muster.bakiye:
                                                    onay = input("""{} adlı müşterimize {} TL para yatırma işlemini 
                                    onaylıyor musunuz? E/H\n""".format(digermusteri.isim, miktar))
                                                    if onay == "E" or onay == "e":
                                                        digermusteri.bakiye += miktar
                                                        Muster.bakiye -= miktar
                                                        print("Para Yatırıldı!")
                                                        gec2()
                                                    elif onay == "H" or onay == "h":
                                                        print("İşlem İptal Edildi!")
                                                        gec2()
                                                    else:
                                                        print("Hatalı Girildi, İşlem İptal Edildi!")
                                                        gec2()
                                                else:
                                                    print("Bakiyeniz bu işlem için yetersiz!")
                                                    gec2()
                                    else:
                                        print("Müşteri bulunamadı!")
                                        gec2()


                                elif sec2 == "4":
                                    miktar = int(input("Çekmek istediğiniz para miktarını giriniz: "))
                                    if miktar <= Muster.bakiye:
                                        onay = input("""{} TL para çekme işlemini 
                                        onaylıyor musunuz? E/H\n""".format(miktar))
                                        if onay == "E" or onay == "e":
                                            Muster.bakiye -= miktar
                                            print("İşlem Tamamlandı, Paranızı Almayı Unutmayın!")
                                            gec3()
                                        elif onay == "H" or onay == "h":
                                            print("İşlem İptal Edildi!")
                                            gec2()
                                        else:
                                            print("Hatalı Girildi, İşlem İptal Edildi!")
                                            gec2()
                                    else:
                                        print("Bakiyeniz bu işlem için yetersiz!")
                                        gec3()

                                elif sec2 == "Q" or sec2 == "q":
                                    print("Çıkış Yapılıyor...")
                                    gec()
                                    break
                        else:
                            print("Hatalı Parola!")
                            gec()
            else:
                print("ID Bulunamadı!")
                gec()

        elif secim == "2":
            ID = input("ID: ")
            AD = input("İSİM: ")
            PAROLA = input("Parola: ")
            banka.muster_ol(AD, ID, PAROLA)

        elif secim == "Q" or secim == "q":
            print("Çıkış yapılıyor...")
            time.sleep(3)
            exit()
        else:
            print("Hatalı Girdiniz!")
            gec()

if __name__ == "__main__":
    main()
