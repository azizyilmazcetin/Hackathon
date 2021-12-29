import hashlib
class dilKontrol():
    
   def kelimeAyirma():
      metin=input("Metin, cümle ya da kelime giriniz:")
      cumle=metin.split(".")
      print("Metindeki Cümleler:",cumle)
      listToStr=''.join([str(elem)for elem in cumle])
      kelime=listToStr.split(" ")
      print("Metindeki Kelimeler:",kelime)
      return metin,cumle,kelime
  
   def sayac(cumle,kelime):
       csayi=len(cumle)
       ksayi=len(kelime)
       print("Metindeki Cümle Sayısı:",csayi)
       print("Metindeki Kelime Sayısı:",ksayi)
       
   def sesliHarfSayisi(metin):
      sesli_harf = 'AEIİOÖUÜaeıioöuü'
      say = 0
      for i in metin:
          if i in sesli_harf:
              say += 1
      print("Metindeki Sesli Harf Sayısı:",say)
   def buyukUnluUyumu(kelime):
       kalin_unluler = list("aıou")
       ince_unluler = list("eiöü")
       uyanSayac=0
       uymayanSayac=0
       for i in range(len(kelime)):
           if (sum(kelime[i].count(kalin) for kalin in kalin_unluler)) != 0 and (sum(kelime[i].count(ince) for ince in ince_unluler)) != 0:
                print(kelime[i]," Büyük Ünlü Uyumuna Uymaz.")
                uymayanSayac=uymayanSayac+1
           else:
                print(kelime[i]," Büyük Ünlü Uyumuna Uyar.")
                uyanSayac=uyanSayac+1
       print("Büyük Ünlü Uyumuna Uyan Kelime Sayısı:",uyanSayac)
       print("Büyük Ünlü Uyumuna Uymayan Kelime Sayısı:",uymayanSayac)
    
   def kucukUnluUyumu(kelime):
       unluler = list("aıoueiöü")
       harfler = []  
       duz_unluler = list("aeıi")  
       duzden_sonra = list("aeıi")
       yuvarlak_unluler = list("ouöü") 
       yuvarlaktan_sonra = list("aeuü")
       kurala_uyuyor = None
       uyanSayac=0
       uymayanSayac=0
       for i in range(len(kelime)):
           kelimeList=kelime[i]
           harfler.clear()
           for harf in kelimeList:
               if harf in unluler:
                   harfler.append(harf)  
    
           for indeks in range(len(harfler)):
                try:
                    if harfler[indeks] in duz_unluler and harfler[
                        indeks + 1] in duzden_sonra: 
                        kurala_uyuyor = True
                    elif harfler[indeks] in yuvarlak_unluler and harfler[
                        indeks + 1] in yuvarlaktan_sonra:  
                        kurala_uyuyor = True
                    else:
                        kurala_uyuyor = False
                        break  
                        
                except IndexError:  
                          continue 
    
           if kurala_uyuyor:
                    print(kelime[i],"Küçük Ünlü Uyumuna Uyar.")
                    uyanSayac=uyanSayac+1
           else:
                    print(kelime[i],"Küçük Ünlü Uyumuna Uymaz.")
                    uymayanSayac=uymayanSayac+1
       print("Küçük Ünlü Uyumuna Uyan Kelime Sayısı:",uyanSayac)
       print("Küçük Ünlü Uyumuna Uymayan Kelime Sayısı:",uymayanSayac)
       
class sifrelemeYontemleri():
    def md5Sifreleme():
        metin=input("Şifrelenecek metin giriniz:")
        hashjob=hashlib.md5()
        hashjob.update(metin.encode())
        print("MD5 Şifrelemesi Uygulanmış Hali:",hashjob.hexdigest())
        return metin
    
    def sha1Sifreleme(metin):
        hashjob=hashlib.sha1()
        hashjob.update(metin.encode())
        print("SHA1 Şifrelemesi Uygulanmış Hali:",hashjob.hexdigest())
        
    def sha224Sifreleme(metin):
        hashjob=hashlib.sha224()
        hashjob.update(metin.encode())
        print("SHA224 Şifrelemesi Uygulanmış Hali:",hashjob.hexdigest())   
        
    def sha256Sifreleme(metin):
        hashjob=hashlib.sha256()
        hashjob.update(metin.encode())
        print("SHA256 Şifrelemesi Uygulanmış Hali:",hashjob.hexdigest())
        
    def sha384Sifreleme(metin):
        hashjob=hashlib.sha384()
        hashjob.update(metin.encode())
        print("SHA384 Şifrelemesi Uygulanmış Hali:",hashjob.hexdigest())
        
    def sha512Sifreleme(metin):
        hashjob=hashlib.sha512()
        hashjob.update(metin.encode())
        print("SHA512 Şifrelemesi Uygulanmış Hali:",hashjob.hexdigest())
        
    def ceaserSifreleme(metin):
        result=""
        for i in range(len(metin)):
            char=metin[i]
            if(char.isupper()):
                result+=chr((ord(char)-64)%26+65)
            else:
                result+=chr((ord(char)+96)%26+97)
        print("Ceaser Şifrelemesi Uygulanmış Hali:",result)
       
class yardim:
    def yazdir():
        yard="dilKontrol sınıfı içerisindeki kelimeAyirma fonksiyonu, girilen metini cümle ve kelimelere ayırır. sayac fonksiyonu ayrılan cümle ve kelimeleri sayar ve ekrana yazdırır. sesliHarfSayisi fonksiyonu girilen metindeki sesli harf sayısını bulup ekrana yazdırır. buyukUnluUyumu fonksiyonu girilen kelimelerin büyük ünlü uyumuna uyup uymadığını kontrol ederek ekrana kelimeleri ve sayısını yazdırır. kucukUnluUyumu fonksiyonu girilen kelimelerin küçük ünlü uyumuna uyup uymadığını kontrol ederek ekrana kelimeleri ve sayısını ekrana yazdırır."
        yard2="sifrelemeYontemleri sınıfı içerisindeki fonksiyonlar girilen metni farklı şifreleme yöntemleri kullanarak şifreler."
        return yard,yard2     
print("=======================")
print("Dil Bilgisi Kontrolü İçin 1")
print("Şifreleme Yöntemleri İçin 2")  
print("Yardım İçin help")
secim = input("Yapılacak İşlemi Seçin:") 
if secim == '1':
   metin,cumle,kelime=dilKontrol.kelimeAyirma()
   dilKontrol.sayac(cumle,kelime)
   dilKontrol.sesliHarfSayisi(metin)
   dilKontrol.buyukUnluUyumu(kelime)
   dilKontrol.kucukUnluUyumu(kelime)
 
elif secim == '2':
   metin2=sifrelemeYontemleri.md5Sifreleme()
   sifrelemeYontemleri.sha1Sifreleme(metin2)
   sifrelemeYontemleri.sha224Sifreleme(metin2)
   sifrelemeYontemleri.sha256Sifreleme(metin2)
   sifrelemeYontemleri.sha384Sifreleme(metin2)
   sifrelemeYontemleri.sha512Sifreleme(metin2)
   sifrelemeYontemleri.ceaserSifreleme(metin2)
elif secim == 'help':
    print("Dil Kontrol Yardımı İçin 1")
    print("Şifreleme Yöntemleri Yardımı İçin 2")
    secim2 = input("Yapılacak İşlemi Seçin.")  
    yard,yard2=yardim.yazdir()
    if secim2=='1':
      print(yard)
    elif secim2=='2':
      print(yard2)
       
       
        

