def presenteer(dictionary,totaal):
    
    uitvoer=""
    for k,v in dictionary.items():
        print(k,":",v, "euro")
    print("==========================")
    print(f"Totaal : {totaal} euro")
    return uitvoer

print(presenteer)