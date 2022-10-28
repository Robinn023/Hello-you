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

def stukje2():
    print("Je pakt een mes uit een la. De gemuteerde stormt door de deur opening en precies wanneer die jou wilt aanvallen gooi je het mes.")
    print(" De mes komt terecht in de been van de gemuteerde en raakt verzwakt. Je trapt het ook nog maar dat was een slecht idee.") 
    print("Je krijgt een harde klap op de gezicht en raakt bijna buiten bewust.") 
    time.sleep(3)
    print("A: A: Aansteker gebruiken")
    print("B: Toch doorvechten")

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
        stukje12()

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
        stukje5

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
    print(" Ik ga het wapen testen. Wat kan er fout gaan. PANG je schiet het wapen zonder na te denken en") 
    print("er vormt een explosie die door de hele buurt te horen is. Dit zorgt gelijk voor meer problemen.") 
    print("Want je ziet meerdere gemuteerde komen. Wat doe je.")
    time.sleep(3)
    print("A: Schieten op de groep gemuteerde")
    print("B: Wegrijden met de auto") 
    vraag = input()
    if vraag in answer_A:
        stukje10()

    elif vraag in answer_B:
        stukje11()
        
    else:
        print("ongeldig antwoord")

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