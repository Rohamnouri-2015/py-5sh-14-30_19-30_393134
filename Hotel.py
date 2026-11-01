



pardakti=[]
while True:
    otagh__hotel=input(" 1.  otagh 564    2. otagh 743   3. exit :")

    while True:
        match otagh__hotel :
            case "1" :
                chand__khab=input(" 1. 2khab = 5640    2. 3khab 743 = 7430 ")
                tedad__2khab= int(input("chan shab ?"))
                gheymat__2khab= chand__khab * 5640 * 1.1
                print(gheymat__2khab)
                
                tedad__3khab=int(input("chan shab ?"))
                gheymat__3khab= chand__khab * 7430 * 1.1
                print(gheymat__3khab)
                pardakti.append(gheymat__2khab)
                pardakti.append(gheymat__3khab)
            case "2" :
                break

            

                

                      