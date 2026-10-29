from daramad import *
from hazine import *
while True:
    gozarsesh__mali=[]
    dastebandee=input("1.variz  2.hazine  3.exit :")
    while True:
        match dastebandee:
            case "1":
                variz__mani=int(input("cheghadr  variz  shod ?"))
                variz=(variz__mani)
            case "2":
                hazine=int(input(" cheghadr koft kardi ?"))
                bardasht=(hazine)
            case "3":
                moojodi__nahaee=variz__mani
                print(moojodi__nahaee)
                break
                            