import datetime


def tänane_kuupäev():
    return datetime.date.today()


def kuupäev_str(kp):
    # saab sisendiks kuupäeva ja tagastab selle sõnena formaadis (pp.kk.aaaa)
    return kp.strftime("%d.%m.%Y")


def arvuta_visiidi_kuupäev(p_külastuse_kuupäev):
    täna = tänane_kuupäev()
    # liidame pool aastat (182 päeva) viimasele külastusele
    uus_visiidiaeg = p_külastuse_kuupäev + datetime.timedelta(182)
    if uus_visiidiaeg <= täna:
        uus_visiidiaeg = täna + datetime.timedelta(1)
    return uus_visiidiaeg


print("Hambaid tuleks lasta kontrollida vähemalt kaks korda aastas.")
print("Millal viimati hambaarsti juures käisid?")

try:
    krokodill = input("Sisesta kuupäev (kujul pp.kk.aaaa): ")
    # logisse kirjutamine vaja teha
    päev, i_kuu, aasta = map(int, krokodill.split('.'))
    külastuse_kuupäev = datetime.date(aasta, i_kuu, päev)

    if külastuse_kuupäev > tänane_kuupäev():
        print("Tulevikus ei saanud visiidil käia.")
    else:
        print("Viimane külastus oli: " + kuupäev_str(külastuse_kuupäev))
        uus_külastus = Arvuta_visiidi_kuupäev(külastuse_kuupäev)
        print("Peaksid minema uuele visiidile umbes: " + kuupäev_str(uus_külastus))
except Exception as verivorst:
    print("Sisestasid kuupäeva vales formaadis!")
    # logisse kirjutamine vaja teha
