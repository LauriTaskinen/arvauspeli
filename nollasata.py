# Peli, jossa arvataan koneen arpoma numero. Kymmenen parasta tulosta listataan tulostauluun
# ja tulostaulu päivittyy sitä mukaa, kun pelejä pelataan.
import random
import os.path
import os

# Globaalit muuttujat. Muuttamalla minNumber ja maxNumber arvoja voidaan
# säätää pelin "vaikeustasoa".
minNumber = 0
maxNumber = 100
guesses = 0
# Pelaajien tiedot tallennetaan väliaikaisesti dictionaryyn, kun tulokset luetaan ulkoisesta tiedostosta.
playerDict = {}
# Ulkoisen tiedoston nimi ja polku tiedostoon.
# Oletuksena tiedosto luodaan Windows käyttäjän kotihakemiston "Documents" -kansioon
filename = "tulokset.txt"
path = os.path.expanduser("~/Documents")
path += "/"
# Alustetaan tyhjä tulokset.txt tiedosto,
# kun sovellus käynnistetään ensimmäistä kertaa.
try:
    with open(path + filename, "a") as file:
        file.write()
        file.close()
except:
    pass
# Funktio tyhjentää komentorivin


def clear(): return os.system('cls')

# Funktio tarkistaa pelaajien tulokset ulkoisesta tulokset.txt tiedostosta
# ja kirjoittaa uusia tuloksia kyseiseen tiedostoon


def write(num):
    uname = x
    result = ""f'{uname}, tulos: {str(num)}\n'""
    try:
        # Luetaan tulokset ulkoisesta tiedostosta ja lisätään ne "playerDict" dictionaryyn
        # Jos pelaaja on saanut ensi tuloksen 10 ja myöhemmin sama pelaaja
        # parantaa tulostaan (arvaa numeron vähemmillä arvauksilla)
        # näkyy hänen parempi tulos ainoastaan dictionaryssä, koska samaa avainta ei voi olla kuin yksi.
        # HUOM! ulkoisessa tiedostossa näykyy edelleen myös pelaajan vanha tulos, mutta sitä ei enää sieltä lueta.
        with open(path + filename, "r") as f:
            for line in f.readlines():
                playerDict[line.split(",")[0].strip()] = int(
                    line.split(':')[1].strip())
        # Jos kyseisellä nimimerkillä ei löydy tulosta, kirjataan tulos tiedostoon.
        if uname not in playerDict:

            file = open(path + filename, "a")
            file.write(result)
            file.close()
        # Verrataan onko kyseisen pelaajan uusi tulos parempi (pienempi luku),
        # kuin saman pelaajan (nimimerkin) edellinen tulos.
        # Jos tulos on parempi, kirjataan se ulkoiseen tiedostoon.
        elif uname in playerDict and playerDict[uname] > num:

            file = open(path + filename, "a")
            file.write(result)
            file.close()
        # Palautetaan tämä jos pelaaja ei parantanut omaa ennätystään.
        else:
            return f'Hyvä yritys, mutta et parantanut omaa ennätystäsi.'
    except:
        print("Tiedoston luonti ja kirjoittaminen epäonnistui")

# Tätä funktiota kutsutaan kun pelaaja haluaa nähdä "kunniataulun" eli top 10 tulokset.


def read():
    try:
        with open(path + filename, "r") as f:
            for line in f.readlines():
                playerDict[line.split(",")[0].strip()] = int(
                    line.split(':')[1].strip())
    except:
        pass


# PÄÄOHJELMA
while guesses == 0:

    print('*** NOLLASATA - ARVAUSPELI ***\n')
    print('[1]: Aloita uusi peli')
    print('[2]: Kunniataulu')
    print('[3]: Ohjeet')
    print('[4]: Sulje peli\n')
    option = input('Mitä tehdään?: ')
    clear()
    # Aloitetaan uusi peli
    if option == "1":
        print("*** Aloitetaan arvauspeli ***\n")
        username = input("Anna ensin nimimerkkisi: ")
        # Tyhjennetään komentorivi käyttäjän syötteen jälkeen selkeämmän käytettävyyden vuoksi.
        clear()
        print(
            f'Hei {username} ja onnea Nollasataan!\nTehtäväsi on arvata valitsemani luku\n')
        print(f'Ajattelen lukua väliltä {minNumber}-{maxNumber}')
        # Arvotaan arvattava numero 0 ja 100 väliltä.
        realValue = random.randrange(0, 100)
        x = username
        # Siirrytään looppiin, jos pelaaja on syöttänyt käyttäjätunnuksen.
        while x == username:
            try:
                answer = int(input('Anna arvauksesi: '))
                clear()
                guess = answer
                if guess > maxNumber or guess < minNumber:
                    guesses += 1
                    print(
                        f'Haha... älä pelleile, luku on väliltä {minNumber}-{maxNumber}')
                elif guess > realValue and guess != realValue:
                    print('Ajattelen pienempää lukua kuin', guess)
                    guesses += 1
                elif guess < realValue and guess != realValue:
                    print('Ajattelen isompaa lukua kuin', guess)
                    guesses += 1
                elif guess == realValue:
                    guesses += 1
                    print(
                        f'Hienoa! Luku oli {guess}. Arvasit sen {guesses} yrittämällä!')
                    write(guesses)
                    # Oletuksena pysäytetään looppi oikean arvauksen jälkeen.
                    x = ""
                    newRound = True
                    # Kysytään haluaako pelaaja pelata uuden pelin.
                    # Jos kyllä, niin pelaajan ei tarvitse syöttää käyttäjätunnustaan uudelleen.
                    while newRound:
                        try:
                            newGame = input('Uusi peli? [y]/[n] ')
                            guesses = 0
                            if newGame == "y" or newGame == "Y":
                                clear()
                                print("*** Aloitetaan arvauspeli ***")
                                print(
                                    f'Hei {username} ja onnea peliin!\nTehtäväsi on arvata valitsemani luku\n')
                                print(
                                    f'Ajattelen lukua väliltä {minNumber}-{maxNumber}')
                                x = username
                                realValue = random.randrange(1, 100)
                                newRound = False
                            # Jos pelaaja haluaa lopettaa pelin, palataan takaisin päävalikkoon.
                            elif newGame == "n" or newGame == "N":
                                clear()
                                break
                            else:
                                continue
                        except:
                            print("Väärä merkki")
                            pass
            except:
                clear()
                print(
                    f'Älä pelleile, anna luku väliltä {minNumber}-{maxNumber}')
                pass
    # Avaa top 10 tulokset ja listaa tulokset.
    elif option == "2":
        print('*** TOP 10 KUNNIATAULU ***\n')
        read()
        number = 1
        # Sortatan dictionaryyn viedyt avain-arvoparit pienimmän arvausmäärän mukaan.
        for key, value in sorted(playerDict.items(), key=lambda x: x[-1])[::1][:10]:
            print(f'{number}. {key}: {value} arvausta ')
            number += 1
        print("\nHUOM yhdellä nimimerkillä voi olla vain yksi tulos! Jos haluat monta tulosta, vaihda nimeäsi ;)")
        menu = input('\nPalaa päävalikkoon painamalla [enter]')
        clear()
        if menu == "":
            guesses = 0
    # Pelin ohjeet.
    elif option == "3":
        print('*** OHJEET ***\n')
        print(
            "Tehtävänäsi on arvata numero 0-100 mahdollisimman vähällä arvausmäärällä.\nJokaisen arvauksen jälkeen peli kertoo oliko arvaamasi numero pienempi vai suurempi, kuin arvattava numero.\nArvattuasi oikean numeron voit aloittaa uuden pelin antamalla syötteen [y] tai lopettaa pelin antamalla syötteen [n].\nParhaat arvaajat pääsevät kunniataululle, joten eikun yrittämään!\nVaikka sinulla olisi useampi kärkitulos näkyy sijoituksesi listassa vain yhden kerran parhaan tuloksesi mukaan.")
        menu = input('\nPalaa päävalikkoon painamalla [enter]')
        clear()
        if menu == "":
            guesses = 0
    # Suljetaan peli syötteellä 4.
    elif option == "4":
        guesses = 1
        print("Suljetaan peli")
