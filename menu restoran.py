



factor=[]
while True:
    menu_restorane=input("1.food   2.drink    3.exit :")
    while True:
      match menu_restorane:
         case"1":
            menu_food=input("1.shshlik=1000     2.kabab=550      3.goge=379 :")
            match menu_food:
                case"1":
                    tedad_shshlik=int(input("chand ta mikhay?"))
                    geymat_shshlik=tedad_shshlik * 1000 * 1.1
                    print(geymat_shshlik)
                case"2":
                    tedad_kabab=int(input("chand ta mikhay :"))
                    geymat_kabab=tedad_kabab * 500 * 1.1
                    print(geymat_kabab)
                case"3":        
                    tedad_goge=int(input("chand ta mikhay :"))
                    geymat_goge=tedad_kabab * 379 * 1.1
                    print(geymat_goge)
                    factor.append(geymat_shshlik)
                    factor.append(geymat_kabab)
                    factor.append(geymat_goge)
                    continue    
         case"2":
             menu_drink=input("1.mohito=250     2.monster=350    3.tea=50 :")
             match menu_drink:
                 case"1":
                    tedad_mohito=int(input("chand ta mikhay :"))
                    geymat_mohito=tedad_mohito * 250 * 1.1
                    print(geymat_mohito)
                 case"2":   
                    tedad_monster=int(input("chand ta mikhay :"))
                    geymat_monster=tedad_monster * 350 * 1.1
                    print(geymat_monster)

                 case"3":    
                    tedad_tea=int(input("chand ta mikhay :"))
                    geymat_tea=tedad_tea * 50 * 1.1
                    print(geymat_tea)

         case"3":
            break
      

            

      

