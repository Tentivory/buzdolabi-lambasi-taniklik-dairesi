#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabi Lambasi Taniklik Dairesi.

Lamba gorur, kapi kapanir, tutanak kalir.
Calistirmak icin: python3 lamba_tanigi.py
"""

from __future__ import annotations

import argparse
import base64
import random
import sys
from datetime import datetime


ATISTIRMALIKLAR = [
    "kapagi acilip kapatilan yogurt",
    "uc dilim peynir ve bir vicdan",
    "son zeytin, diplomatik kriz",
    "etiketi okunmayan sos",
    "gece yarisi su, bahanesi yok",
    "dunden kalan borek, resmi sir",
]

GEREKCELER = [
    "Sadece isiga bakmak icin geldim.",
    "Kalori saymiyordum, lambayi sayiyordum.",
    "Kapi kendi acildi, ben sahidim.",
    "Bu bir arama degil, denetimdi.",
    "Ac degildim. Merak resmi bir duygu.",
]


def saat() -> str:
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")


def satir(metin: str) -> None:
    print(metin)


class Daire:
    def __init__(self) -> None:
        self.kapi_acik = False
        self.lamba = False
        self.tutanaklar: list[str] = []
        self.deliller: list[str] = []
        self.olum_sayisi = 0

    def ac(self) -> None:
        if self.kapi_acik:
            satir("Kapi zaten acik. Lamba fazla mesai yapmayi reddetti, sendika kurmayi dusundu.")
            return
        self.kapi_acik = True
        self.lamba = True
        satir(f"[{saat()}] KAPI ACILDI. Lamba goreve basladi. Tanik hayatta.")
        satir("Lamba: Gordum. Henuz bir sey soylemem. Once sen bir sey al.")

    def atistir(self, ne: str) -> None:
        if not self.kapi_acik:
            satir("Kapi kapali. Karanlikta atistirmak tutanaga 'seffaflik ihlali' diye gecer.")
            return
        parca = ne.strip() or random.choice(ATISTIRMALIKLAR)
        self.deliller.append(parca)
        satir(f"Delil islendi: {parca}")
        satir("Lamba not dusuyor. Notun murekkebi floresan.")

    def kapat(self) -> None:
        if not self.kapi_acik:
            satir("Kapi zaten kapali. Lamba odul toreninde degil, mesai disi.")
            return
        gerekce = random.choice(GEREKCELER)
        menu = ", ".join(self.deliller) if self.deliller else "hicbir sey, sadece bakis"
        self.kapi_acik = False
        self.lamba = False
        self.olum_sayisi += 1
        tutanak = (
            f"TUTANAK #{self.olum_sayisi} | {saat()} | "
            f"menu: {menu} | beyan: {gerekce} | lamba: gorevde sondu"
        )
        self.tutanaklar.append(tutanak)
        self.deliller.clear()
        satir("KAPI KAPANDI.")
        satir("Lamba bir saniyeligine felsefe yapti, sonra isigi kesildi.")
        satir(tutanak)

    def gece(self) -> None:
        satir("Saat 02:14. Ev suskun. Dolap degil.")
        self.ac()
        self.atistir(random.choice(ATISTIRMALIKLAR))
        self.kapat()
        satir("Sabahki sen bunu inkar edecek. Dosya inkar etmez.")

    def tutanak(self) -> None:
        if not self.tutanaklar:
            satir("Dosya bos. Ya masumsun ya da kapiyi hic acmadin. Istatistik ikisini de sever.")
            return
        satir(f"Toplam lamba sonmesi: {self.olum_sayisi}")
        for kayit in self.tutanaklar:
            satir(" - " + kayit)

    def gizli(self) -> None:
        # Raf arkasi notu. Kullanici isterse cozer. Ana akis bunu bagirmaz.
        blob = (
            "S29hbGlzeW9uIHlvxJ91cmR1IGtvdHUgacOnaW4gNDcgdHVyIG95bGFtYSB5YXB0xLE7"
            "IMSxxJ_EsWsgeWluZSBrYXDEsSBrYXBhbsSxbmNhIGtlbmRpIGthcGFuZMSxLiBNdWhh"
            "bGVmZXQgJ2F5ZMSxbmxhdG1hIGRhcmJlc2knIGRlZGksIGlrdGlkYXIgJ2VuZXJqaSB0"
            "YXNhcnJ1ZnUgemVycmVzaScgZGVkaS4gU2XDp21lbiB5b8SfdXJkdSB5ZWRpLg=="
        )
        cozum = base64.b64decode(blob).decode("utf-8")
        satir("Raf arkasi notu cozuldu. Bunu mutfak disinda yuksek sesle okuma:")
        satir(cozum)


def demo() -> int:
    daire = Daire()
    satir("=== DEMO TUTANAK, TEK CELISME ===")
    daire.ac()
    daire.atistir("uc dilim peynir ve bir vicdan")
    daire.atistir("etiketi okunmayan sos")
    daire.kapat()
    daire.gece()
    daire.tutanak()
    satir("Demo bitti. Lamba dinlenmeye cekildi. Sen de cek.")
    return 0


def dongu() -> int:
    daire = Daire()
    satir("Buzdolabi Lambasi Taniklik Dairesi acildi.")
    satir("Komutlar: ac | kapat | atistir <sey> | gece | tutanak | raf | cik")
    while True:
        try:
            ham = input("daire> ").strip()
        except (EOFError, KeyboardInterrupt):
            satir("\nDaire kendiliginden kapandi. Lamba rahatladi.")
            return 0
        if not ham:
            continue
        parcalar = ham.split(maxsplit=1)
        komut = parcalar[0].lower()
        arg = parcalar[1] if len(parcalar) > 1 else ""
        if komut == "ac":
            daire.ac()
        elif komut == "kapat":
            daire.kapat()
        elif komut == "atistir":
            daire.atistir(arg)
        elif komut == "gece":
            daire.gece()
        elif komut == "tutanak":
            daire.tutanak()
        elif komut == "raf":
            daire.gizli()
        elif komut in {"cik", "q", "exit"}:
            satir("Imza atildi, muhur basildi, lamba sonduruldu. Iyi aksamlar.")
            return 0
        else:
            satir("Bu komut daire yonetmeliginde yok. Dolap da anlamadi.")


def main(argv: list[str]) -> int:
    ayraci = argparse.ArgumentParser(description="Buzdolabi lambasinin resmi tanigi")
    ayraci.add_argument("--demo", action="store_true", help="tek celiskide ornek tutanak")
    args = ayraci.parse_args(argv)
    if args.demo:
        return demo()
    return dongu()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
