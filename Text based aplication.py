from secrets import choice
import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]

def stukje1():
    print("Je opent de raam en schreeuwt tegen de gemuteerde in de hoop om het bang te maken.")
    print(" Maar in tegendeel maak het schreeuwen de gemuteerde alleen maar kwaaier.")  
    print("De gemuteerde schreeuwt terug en trapt tegen de deur. Vol angst probeer je het weg te jagen maar niks helpt.")
    print(" De gemuteerde breekt binnen en zoekt je. Wat doe je:")
    time.sleep(3)
    print("A: Vechten met de gemuteerde")
    print("B: Jezelf opsluiten in je kamer")
    vraag = input()
    if vraag in answer_A: 
        stukje2()

    elif vraag in answer_B:
        stukje3()

    else:
        print("ongeldig antwoord")

def stukje2():
    print("Je pakt een mes uit een la. De gemuteerde stormt door de deur opening en precies wanneer die jou wilt aanvallen gooi je het mes.")
    print(" De mes komt terecht in de been van de gemuteerde en raakt verzwakt. Je trapt het ook nog maar dat was een slecht idee.") 
    print("Je krijgt een harde klap op de gezicht en raakt bijna buiten bewust.") 
    time.sleep(3)
    print("A: A: Aansteker gebruiken")
    print("B: Toch doorvechten")
    vraag = input()
    if vraag in answer_A: 
        stukje12()

    elif vraag in answer_B:
        einde1()

    else:
        print("ongeldig antwoord")

def einde1():
    print("Na de harde klap gaf je niet op en probeerde alles om de gemuteerde te verslaan.") 
    print("Maar je hielt het niet lang vol en ging na een kort maar pijnlijk gevecht viel je neer. Je bent verslagen en ging DOOD.")
    print("Game over")

 
def stukje3():
    print("Je verstopt in je kamer (weg van het raam). Je wacht en wacht.") 
    print("Na een kwartier wachten wat voelde als een uur gluurde je door het raam.") 
    print("Je haalde diep adem en was opgelucht om te zien dat het monster weg was. Maar niet voor lang. wat ga je doen")
    time.sleep(3)
    print("A: Onderzoek doen")
    print("B: Op zoek gaan naar de gemuteerde")
    vraag = input()
    if vraag in answer_A: 
        stukje4()

    elif vraag in answer_B:
        stukje14()

    else:
        print("ongeldig antwoord")

def stukje4():
    print("Je wist niet wat je had gezien dus ga je onderzoek plegen. Je pakt je slippers en loopt naar buiten om te kijken of de gemuteerde iets heeft achtergelaten.")
    print("Niks gevonden denk je, maar net voor dat je naar binnen gaat zie je wat vreemds liggen. Je raapt het op en het voorwerp blijkt een") 
    print("handwapen te zijn van de gemuteerde. Nieuwsgierig breng je het wapen naar binnen en analyseer je het. Wat doe je met het wapen:")
    time.sleep(3)
    print("A: Scannen voor vingerafdrukken ")
    print("B: Het wapen uittesten ")
    vraag = input()
    if vraag in answer_A: 
        stukje8()

    elif vraag in answer_B:
        stukje5()

    else:
        print("ongeldig antwoord")


def stukje5():
    print("Natuurlijk gaan we het wapen uittesten, kijken hoe krachtig het is. Je puzzelt om erachter te komen hoe het wapen werkt.")
    print("Blijkt best simpel want het werkt bijna het zelfde als een pistool. Waar ga je het testen:")
    time.sleep(3)
    print("A: Binnen")
    print("B: Buiten")
    vraag = input()
    if vraag in answer_A: 
        stukje6()

    elif vraag in answer_B:
        stukje6()

    else:
        print("ongeldig antwoord")

def stukje6():
    print("Ik ga het wapen testen. Wat kan er fout gaan. PANG je schiet het wapen zonder na te denken en") 
    print("er vormt een explosie die door de hele buurt te horen is. Dit zorgt gelijk voor meer problemen.") 
    print("Want je ziet meerdere gemuteerde komen. Wat doe je.")
    print("A: Schieten op de groep gemuteerde")
    print("B: Wegrijden met de auto")
    vraag = input()
    if vraag in answer_A: 
        stukje10()

    elif vraag in answer_B:
        stukje11()

    else:
        print("ongeldig antwoord")

def stukje7():
    print(": Slim gedaan. Het vuur maakt de gemuteerde bang en je bent voor nu veilig.") 
    print("Je checkt later of het wat heeft achtergelaten en je vind een wapen. Wat doe je.")
    print("A: Onderzoek plegen")
    print("B: Schieten met het wapen")
    vraag = input()
    if vraag in answer_A: 
        stukje9()

    elif vraag in answer_B:
        stukje6()

    else:
        print("ongeldig antwoord")

def stukje8():
    print("Je trekt handschoenen aan en scant het wapen voor mogelijke vingerafdrukken.") 
    print("Er zitten inderdaad afdrukken op van de gemuteerde en het zijn grote afdrukken. Wat doe je:")
    print("A: zelf uittesten hoe het monster er uit moet zien en uit wat het bestaat")
    print("B: Het wapen naar een laboratorium sturen ")
    vraag = input()
    if vraag in answer_A: 
        stukje9()

    elif vraag in answer_B:
        stukje9()

    else:
        print("ongeldig antwoord")

def stukje9(): 
    print("Je komt te weten dat de gemuteerde niet altijd het zelfde was.") 
    print("Het is ooit een mens geweest want er zit DNA van een mens in. Het bestaat")
    print("grotendeels uit een onbekende metaal en water. Het is 1.5 keer zo groot als een mens.") 
    print("Een zwaktepunt van de gemuteerde is vuur.") 
    print("Nu je weet wat het zwaktepunt is wil je op zoek gaan naar de gemuteerde in de grot.")
    print("Wat neem je mee")
    print(" A: Vlammenwerper")
    print(" B: gemuteerde pistool")
    vraag = input()
    if vraag in answer_A: 
        stukje14()

    elif vraag in answer_B:
        stukje14()

    else:
        print("ongeldig antwoord")

def stukje10():
    print("Je gaat vol in actie en schiet op de groep gemuteerde. Je schiet een in het hoofd, de ander in het hart.")
    print(".  Je begint goed maar ze komen al snel dichtbij en van alle kanten.") 
    print("Met enorme vaart springen gemuteerde van gebouw naar gebouw.")
    print("Maar je bent ze te slim af en schiet op de gastank op het dak en explodeert de gemuteerde op het dak.")
    print("het hele gebouw stort daarna in. Van rechts komen er een paar met wapens. Wat doe je")
    print(" A: hun schieten") 
    print(" B: Achter auto schuilen")
    vraag = input()
    if vraag in answer_A: 
        stukje19()

    elif vraag in answer_B:
        stukje20()

    else:
        print("ongeldig antwoord")

def stukje11():
    print("Je pakt zo snel mogelijk de sleutels en boekt hem met de auto.") 
    print("Plankgas scheur je want de gemuteerde volgen en schieten op je.") 
    print("Met enorme geluk ontwijk je de meeste kogels,") 
    print("maar nu komt er nader je een brug waar een grote gemuteerde 5 meter groot je op wacht. Wat doe je.")
    print(" A: plankgas doorrijden en hopen door de gemuteerde te breken")
    print(" B: Het modderweg nemen naar het bos")
    print(" C: Opgeven")
    vraag = input()
    if vraag in answer_A: 
        stukje12()

    elif vraag in answer_B:
        einde2()

    elif vraag in answer_C:
        einde3()
    else:
        print("ongeldig antwoord")

def einde2():
    print("Je rijdt over de modderweg tussen al de chaos maar de weg loopt dood.")
    print("Zonder enige mogelijkheid om te ontsnappen wordt je neergeschoten door een raket.")
    print("Je ging DOOD!")

def einde3():
    print("Je ziet het niet meer zitten. Je geeft op en laat het lot liggen. Je ging DOOD!")

def stukje12():
    print("Je rijdt recht op de gemuteerde die op de brug  staat.") 
    print("Hij kijkt naar je. Je komt dichterbij en dichterbij. De grote gemuteerde springt om op je te stampen,") 
    print(" maar je rijd er net onderdoor met mega veel geluk. De gemuteerde valt ook nog. Wat doe je")
    print(" A: Doorrijden om te vluchten")
    print(" B: Het leger inschakelen.")
    vraag = input()
    if vraag in answer_A: 
        stukje13()

    elif vraag in answer_B:
        einde4()

    else:
        print("ongeldig antwoord")

def einde4():
    print("Je schakelt het leger in en binnen 10 minuten zijn er gevecht helikopters gearriveerd.") 
    print("Er breekt een volledige oorlog uit. Maar de helikopters worden neergeschoten.") 
    print("Dit zorgt ervoor dat er genoeg tijd is dat er gevecht tanken komen en winnen het gevecht en schieten alle gemuteerde neer.") 
    print("Na een half uur is het gewonnen. Iedereen is opgelucht en er is een vredig einde. goed gedaan!") 

def stukje13():
    print("Je rijdt weg en ontsnapt maar je hebt niks behalve je auto.")
    print("A: Vluchten naar België ")
    print("B: Vluchten naar Duitsland")
    vraag = input()
    if vraag in answer_A: 
        einde5()

    elif vraag in answer_B:
        einde5()

    else:
        print("ongeldig antwoord")
def einde5():
    print("Je bent ontsnapt maar je moet weer helemaal opnieuw beginnen. Slecht einde")

def stukje14():
    print("Je wilt graag weten waar de gemuteerde vandaan komen na een enge incident.") 
    print("Je pakt de sleutels van de auto en rijdt naar de grote grot 5 kilometer verderop.") 
    print("Bij aankomst stap je uit de auto. Je hebt ook een wapen meegenomen voor de zekerheid.") 
    print("Je weet het maar nooit. Je gaat in de grot in de hoop wat buitenaards te vinden.") 
    print("Net wanneer je binnenloopt sluit en plots een geheime deur achter je. Wat doe je")
    print("Aa: Zo snel mogelijk verstoppen en kijken naar opties")
    print("B: De deur proberen te openen")

    vraag = input()
    if vraag in answer_A: 
        stukje15()

    elif vraag in answer_B:
        einde6()

    else:
        print("ongeldig antwoord")

def stukje15():
    print("Je ziet naast je een doos staan waar je in past. Ga je in de doos verstoppen")
    print("A: Ja")
    print("B: nee, verder zoeken")
    vraag = input()
    if vraag in answer_A: 
        stukje18()

    elif vraag in answer_B:
        stukje16()

    else:
        print("ongeldig antwoord")

def stukje16():
    print("Je denkt niet dat de doos een goede verstopplek is, dus zoek je verder en je ziet een luik aan de muur.")
    print("Je probeert in de luik te klimmen. Het lukt om te klimmen en je bent er bijna.")
    print(" Maar toen werd je naar beneden getrokken door een gemuteerde.") 
    print("Je wordt naar een cel meegenomen en opgesloten. Wat doe je")
    print("A: Smeken om vrij gelaten te worden")
    print("B: proberen om te ontsnappen")
    vraag = input()
    if vraag in answer_A: 
        einde6()

    elif vraag in answer_B:
        einde6()

    else:
        print("ongeldig antwoord")

def einde6():
    print("Je wordt gevonden door een gemuteerde. Je probeert op hem te schieten maar het is te laat.") 
    print("Je wordt meegesleurd door een gemuteerde naar een cel. Je Probeert alles wat je kan bedenken om uit de cel")
    print("te komen maar niks helpt.")
    print("Je bent gevangen!Game over")

def stukje18():
    print(": Je gaat de doos in en je beweegt je geen moer. Muisstil wacht je in de doos.") 
    print("Er komt een gemuteerde die de doos optilt waar jij in zit. Je hart gaat tekeer.") 
    print("De gemuteerde had niks door en de doos wordt weer neergezet. Je wacht nog een tijdje.") 
    print(" Je gluurt uit de doos en het blijkt voor nu veilig te zijn. Je stapt uit de doos en wauw.") 
    print("Er is een enorme glinsterend Crystal.  Je denkt dat het misschien de bron van leven is van de gemuteerde.") 
    print("Wat doe je") 
    print("A: De Crystal slopen") 
    print("B: De kamer verkennen")
    vraag = input()
    if vraag in answer_A: 
        einde7()

    elif vraag in answer_B:
        einde6()

    else:
        print("ongeldig antwoord")

def einde7():
    print("Je slaat met een gemuteerde spies die je zojuist heb gevonden.") 
    print("Je blijft en blijft slaan en steken in de crystal en er beginnen al scheuren te vormen.")
    print("Na een paar minuten bereik je een andere laag. Je slaat erop en plots is er enorme brand.") 
    print("Je trekt terug en rent maar alles ontploft en alles in de grot gaat kapot. Jij en de gemuteerde zijn DOOD")

def stukje19(): 
    print("Je ziet de gemuteerde aankomen en schiet ze. Je raakt eentje en") 
    print("de andere gemuteerde schiet terug schramt je met zijn wapen.") 
    print("Je sprint een gebouw binnen en schiet de andere gemuteerde via een raampje.") 
    print("Nog meer gemuteerde zijn onderweg. Je schiet veel op ze en dat jaagt ze weg. Je ziet ze ook niet meer terug komen na een uur.") 
    print("Je hebt hun verjaagt en ze gaan niet meer vechten met jou. Wat doe je")
    print("A: feestje vieren")
    print("B: dansen")
    vraag = input()
    if vraag in answer_A: 
        stukje21()

    elif vraag in answer_B:
        stukje21()

    else:
        print("ongeldig antwoord")


        
def stukje20():
    print("Je schuilt achter de auto maar de auto gaat al snel in brand. Je vlucht naar een ladder en gaat op een dak.")
    print("Je knalt een gemuteerde af en de andere schiet terug. Je wordt net niet geraakt.") 
    print("Toen schramde je de gemuteerde en rende hij weg. Je hebt gewonnen en ze komen niet meer terug")
    print("A: het succes vieren")
    print("B: dance moves")

def stukje21():
    print("Je viert een groot feest voor jezelf. Top gedaan dat gevecht. Je verdient dit feestje. EINDE van het spel")




def intro():
    print("Je kijkt je favoriete programma en schrik je plotseling van een harde bonk op de deur.")
    print("Je besluit via het boven raam te kijken wie het is.") 
    print("Het was geen bekend persoon, het lijkt wel op een raar gemuteerde mens.")
    time.sleep(1) 
    print("Je kijkt recht in de ogen van de gemuteerde.") 
    print("Met angst staar je naar het, totdat de gemuteerde zijn hoofd langzaam") 
    print( "en griezelig draait. Het heeft je gezien, wat doe je")
    time.sleep(3)
    print("A: Weglopen van het raam en verstoppen ")
    print("B: Het monster proberen weg te jagen ")

    vraag = input()
    if vraag in answer_A: 
        stukje3()

    elif vraag in answer_B:
        stukje1()

    else:
        print("ongeldig antwoord")

intro()