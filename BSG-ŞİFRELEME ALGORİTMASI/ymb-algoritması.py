"""ALGORİTMANIN ÇALIŞMA MANTIĞI:

-----------------------------

1-)COLLATZ-CONJECTURE MANTIĞI:

A-Girilen sayi eğer çiftse n=n/2

B-Girilen sayi tek ise n=3*n+1

------------------------------

2-)YMB ALGORİTMASININ ÇALIŞMA MANTIĞI:

A-Öğrenci nosu'nun son 2 hanesi collatz conjecture a girer ve örüntüdeki tek sayilar 1

çift sayilar ise 0 ile ifade edilir, çift ve tek sayilarin adedi tutulur.

B-)TC nosu'nun son 2 hanesi collatz conjecture a girer ve örüntüdeki tek sayilar 1

çift sayilar ise 0 ile ifade edilir, çift ve tek sayilarin adedi tutulur.

C-)Elde edilen çift ve tek sayilarin adedi(tc ve öğrenci no ile yapilan collatzlarda ayri ayri yapilicak )

binarye(2li sistem)çevirilir,tek ve çift sayilarin adedinden oluşan binary sayilar kendi aralarinda XOR'lanir.

D-)Daha sonra öğrenci ve TC nodan oluşan XOR'lanmiş sayilar son olarak kendi aralarinda XOR'lanir.

E-)Çikan XOR'lanmiş sayi bizim keyimiz oluyor."""


def collatz_stats(n):

    evens, odds = 0, 0
    while n != 1:
        if n % 2 == 0:
            evens += 1
            n //= 2
        else:
            odds += 1
            n = 3 * n + 1
    odds += 1
    return evens, odds

def xor_cipher(text, key):
    """Metni verilen key ile XOR'layarak şifreler veya çözer."""
    return "".join(chr(ord(char) ^ key) for char in text)

def main():
    try:
        print("--- YMB (Collatz tabanlı) Şifreleme Sistemi ---")
        og_no = int(input("Öğrenci No (Son 2 hane): "))
        tc_no = int(input("TC No (Son 2 hane): "))
        mesaj = input("Şifrelenecek metni girin: ")

        # 1. Anahtar Türetme (Senin Algoritman)
        og_e, og_o = collatz_stats(og_no)
        res_a = og_e ^ og_o
        
        tc_e, tc_o = collatz_stats(tc_no)
        res_b = tc_e ^ tc_o
        
        final_key = res_a ^ res_b
        
        print(f"\n[Sistem] Üretilen Anahtar: {final_key} (Binary: {bin(final_key)[2:]})")

        # 2. Şifreleme
        sifreli_metin = xor_cipher(mesaj, final_key)
        print(f"[+] Şifreli Metin: {sifreli_metin}")

        # 3. Deşifreleme
        cozulmus_metin = xor_cipher(sifreli_metin, final_key)
        print(f"[+] Deşifre Edilen Metin: {cozulmus_metin}")

        # 4. Bit Değişimi Testi (Avalanche Effect)
        print("\n" + "="*40)
        print("BİT DEĞİŞİMİ TESTİ (Anahtar 1 bit değişirse ne olur?)")
        
        # Anahtarın son bitini ters çevirelim (XOR 1)
        hatali_key = final_key ^ 1 
        hatali_metin = xor_cipher(sifreli_metin, hatali_key)
        
        print(f"Gerçek Key: {final_key} -> {bin(final_key)}")
        print(f"Hatali Key: {hatali_key} -> {bin(hatali_key)}")
        print(f"Hatali Key ile sonuç: {hatali_metin}")
        print("="*40)

    except ValueError:
        print("Hata: Geçerli sayılar girin!")

if __name__ == "__main__":
    main()