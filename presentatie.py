def presenteer(dictionary,totaal):
    
    uitvoer=""
    for k,v in dictionary.items():
        print(k,":",v, "euro")
    print("==========================")
    print(f"totaal : {totaal} euro")
    return uitvoer

print(presenteer)