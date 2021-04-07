import datetime


def tänane_kuupäev():
    return datetime.date.today()


def kuupäev_str(p_kuupäev):
    # saab sisendiks kuupäeva ja tagastab selle sõnena formaadis (pp.kk.aaaa)
    return p_kuupäev.strftime("%d.%m.%Y")


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
    sisestatud_kuupäev = input("Sisesta kuupäev (kujul pp.kk.aaaa): ")
    # logisse kirjutamine vaja teha
    i_päev, i_kuu, i_aasta = map(int, sisestatud_kuupäev.split('.'))
    külastuse_kuupäev = datetime.date(i_aasta, i_kuu, i_päev)

    if külastuse_kuupäev > tänane_kuupäev():
        print("Tulevikus ei saanud visiidil käia.")
    else:
        print("Viimane külastus oli: " + kuupäev_str(külastuse_kuupäev))
        uus_külastus = arvuta_visiidi_kuupäev(külastuse_kuupäev)
        print("Peaksid minema uuele visiidile umbes: " + kuupäev_str(uus_külastus))
except Exception as error:
    print("Sisestasid kuupäeva vales formaadis!")
    # logisse kirjutamine vaja teha
