# variabelen
Ja = ["Ja"]
Nee = ["Nee"]

# hier worden de functions gedefined

def verhaal_1():
    keuze = input("Ga je opzoek naar je familie Ja/Nee? ")

    if keuze == "Ja":
        print("je gaat opzoek naar je familie.")
        verhaal_2()
    elif keuze == "Nee":
        print("Je gaat niet naar je famillie opzoek.")
        verhaal_3()
    else:
        print("dit is geen geldige keuze antwoord met Ja of Nee")
        verhaal_1()

def verhaal_2():
    print("Je rent naar je afgebrokkelde huis en begint het puin weg te halen.")
    keuze = input("Ga je om hulp vragen Ja/Nee? ")
    
    if keuze == "Ja":
        print("Je roept voor hulp.")
        verhaal_4()
    elif keuze == "Nee":
        print("je kiest ervoor om het alleen te doen.")
        verhaal_5()
    else:
        print("dit is geen geldige keuze antwoord met Ja of Nee")
        verhaal_2()


def verhaal_3():
    print("je gaat alleen op pad.")  
    keuze = input("Een man verzoekt om je te gaan helpen acepteer je de hulp J/Nee? ")
    
    if keuze == "Ja":
        print("De man helpt je om in Nederland te komen.")
        verhaal_6()
    elif keuze == "Nee":
        print("je acepteerd zijn hulp niet en loopt verder")
        verhaal_7()
    else:
        print("dit is geen geldige keuze antwoord met Ja of Nee")
        verhaal_3()


def verhaal_4():
    print("mensen hebben je gehoord en komen je helpen.")  
    keuze = input("je hebt je familie gevonden wat ga je nu doen je gaat met je familie op PAD of je VERZAMELT je bij de rest van het dorp. ")
    
    if keuze == "PAD":
        print("je gaat met je familie op pad opzoek naar hulp.")
        verhaal_8()
    elif keuze == "VERZAMELT":
        print("je verzamelt je met de rest van het dorp en helpt elkaar.")
        verhaal_9()
    else:
        print("dit is geen geldige keuze antwoord met PAD of VERZAMELT")
        verhaal_4()


def verhaal_5():
    print("je haalt in je eentje het puin weg maar er is geen succes")  
    keuze = input("je hebt geen succes met het zoeken van je familie wat ga je doen je maakt er een EINDE aan want je kan niet zonder ze leven of je gaat voor VRAAK. ")
    
    if keuze == "EINDE":
        print("je maakt een einde aan je leven.")
        
    elif keuze == "VRAAK":
        print("je neemt vraak voor je familie en gaat het verzet in")
        verhaal_10()
    else:
        print("dit is geen geldige keuze antwoord met EINDE of VRAAK")
        verhaal_5()


def verhaal_6():
    print("je bent nu in Nederland je bent nu een stapje dichterbij veiligheid.")  
    keuze = input("wat ga je doen je gaat opzoek naar HULP of je gaat gewoon RONDLOPEN. ")
    
    if keuze == "HULP":
        print("je gaat opzoek naar hulp.")
        verhaal_11()
    elif keuze == "RONDLOPEN":
        print("je gaat hulpeloos rondlopen door Nederland.")
        verhaal_12()
    else:
        print("dit is geen geldige keuze antwoord met PAD of VERZAMELT")
        verhaal_6()












































keuze = input("klik op enter om te starten")
print ("Ik woon in een mooi huis meet mijn gezin")
print ("Op een dag ging ik naar mijn werk en toen was mijn huis weg")
verhaal_1()

