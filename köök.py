import datetime


def tänane_kuupäev():
    # Tagastab tänase kuupäeva.
    return datetime.date.today()


def kuupäev_str(p_kuupäev):
    # Saab sisendiks kuupäeva ja tagastab selle sõnena formaadis (pp.kk.aaaa)
    return p_kuupäev.strftime("%d.%m.%Y")


def arvuta_visiidi_kuupäev(p_külastuse_kuupäev):
    # Saab sisendiks viimase visiidi kuupäeva ja tagastab järgmise visiidi aja.
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
    with open("log.txt", "a") as log:
        log.write('[{kellaaeg}] kasutaja sisestas kuupäeva: {sisend}\n'.format(kellaaeg=str(datetime.datetime.now()), sisend=str(sisestatud_kuupäev)))
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
    with open("log.txt", "a") as log:
        log.write('[{kellaaeg}] {error}\n'.format(kellaaeg=str(datetime.datetime.now()), error=str(error)))

