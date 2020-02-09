# the docs for the format:  https://docs.google.com/spreadsheets/d/1LGEnOfUu5PjuE42dMoEhIRve5rv3vNsBtk-8DWozwdg/edit?ts=5e322488#gid=870428257
# https://docs.google.com/spreadsheets/d/1raDs8m-Yd_XOFskueqqcMcMxvR2KVhTJg6ILsQXBhnw/edit#gid=121665415
import codecs
from datetime import datetime
now = datetime.now() # current date and time

#check if the sting contains a number or not;
def hasNumbers(inputString): return any(char.isdigit() for char in inputString)


amazon_unshipped_file = "20010713268018298.txt"

file_stream = codecs.open(amazon_unshipped_file, 'r', 'utf-8')
pdp_file = codecs.open("20010713268018298.csv", 'w', 'utf-16')
pdp_first_line = "Action;ItemID;TransactionID;ShippingStatus;ShippingCarrierUsed;ShipmentTrackingNumber;Firma;Name;Strasse;Adresszusatz;PLZ;Ort;Land;Telefon;E-Mail;KundenNr;Referenz;Inhalt;Gewicht;Nachnahmebetrag;Versanddatum;StatusdatumAbgeholt;StatusdatumZugestellt;PaketstatusID \n"
pdp_file.write(pdp_first_line) # first write the first line into file:

#https://docs.google.com/spreadsheets/d/1raDs8m-Yd_XOFskueqqcMcMxvR2KVhTJg6ILsQXBhnw/edit#gid=121665415 check here, you will see the mappings.
sku_dpd_reference_pairs = {
    "1000":"302008",
    "1001":" ",
    "1002":"160007",
    "1003":"160011",
    "1004":"2020024",
    "1005":"270013",
    "1006":"heater",
    "1007":"BDZ-168",
    "1012":"700023",
    "1013":"270019+270004",
    "1014":"famb008x",
    "1015-L":"302014",
    "1015-M":"302013",
    "1016":"302009",
    "1017":"302012",
    "1019-Basic":"700016",
    "1019-Pro":"302011",
    "1020-3S":"270039",
    "1020-5S":"270038+270039",
    "1021":"190038",
    "1022":"302002",
    "1023":"  ",
    "1024":"302010",
    "1025":"160013",
    "1026-Advance":"Boat-C",
    "1026-Basic":"Boat-A",
    "1026-Mini":"Boat-Mini",
    "1026-Pro":"Boat-D",
    "1027":"160019",
    "1028":"160004",
    "1029":"160010",
    "1030-270":" ",
    "1030-290":" ",
    "1031-180":" ",
    "1031-235":" ",
    "1032-Set":"210017-Set",
    "1032-Standard":"210017-Standard",
    "1032-Winterskin":"210017-Winterskin",
    "1033":"270036",
    "1034":"270038",
    "1035-Set":"210011-Set",
    "1035-Standard":"210011-Standard",
    "1035-Winterskin":"210011-Winterskin",
    "1036-Single":"260003",
    "1036-Double":"260004",
    "1037-Classic":"059NEW+DLeg",
    "1037-Comfort":"059AD(270001)",
    "1037-Comfort-Camouflage":"270005-Camo",
    "1037-Deluxe":" ",
    "1038-Classic":" ",
    "1038-Comfort":" ",
    "1038-Deluxe":" ",
    "1039-Camouflage":"4000SK-Camo",
    "1039-Schwarz":"4000SK-Black",
    "1040-Camouflage":"6000sk -Camo",
    "1040-Schwarz":"6000sk -Black",
    "1041-R1":"Trolley-051-1W",
    "1041-R2":"Trolley-051-2W",
    "1042-001":"10 ft 2 teilig 2.75 lbs-Camo",
    "1042-002":"10 ft 2 teilig 2.75 lbs-Black",
    "1042-003":"10 ft 2 teilig 3 lbs-Camo",
    "1042-004":"10 ft 2 teilig 3 lbs-Black",
    "1042-005":"10 ft 3 teilig 2.75 lbs-Camo",
    "1042-006":"10 ft 3 teilig 2.75 lbs-Black",
    "1042-007":"10 ft 3 teilig 3 lbs-Camo",
    "1042-008":"10 ft 3 teilig 3 lbs-Black",
    "1042-009":"12 ft 3 teilig 3 lbs-Camo",
    "1042-010":"12 ft 3 teilig 3 lbs-Black",
    "1042-011":"12 ft 3 teilig 3.5 lbs-Camo",
    "1042-012":"12 ft 3 teilig 3.5 lbs-Black",
    "1043-LG":"FL-01-Green-Large",
    "1043-LS":"FL-01-Black-Large",
    "1043-MG":"FL-01-Green-Small",
    "1043-MS":"FL-01-Black-Small",
    "1044-Classic 696921":"270016",
    "1044-Comfort 736120":" ",
    "1044-Comfort 746523":" ",
    "1044-Comfort 786821":" ",
    "1044-Deluxe 716521":"  ",
    "1044-Deluxe 736319":" ",
    "1044-Transporttasche":" ",
    "1045-PARENT":"270020",
    "2x-KD4H-M022":"FA214-4+4SW02",
    "AP-978G-XXFK":"270005",
    "C9-KRTX-RO2C":"270025",
    "JX-9LRX-UUZA":"FA02-4"
}

i = 0
for l in file_stream:
    i=i+1
    if (i==1): # not need the first line
        None
    else:
        list_from_amzon = l.split("\t")
        recipient_name = list_from_amzon[16]
        ship_address_1 = list_from_amzon[17]
        ship_address_2 = list_from_amzon[18]
        ship_address_3 = list_from_amzon[19]
        ship_postal_code =list_from_amzon[22]
        ship_city =list_from_amzon[20]
        ship_country =list_from_amzon[23].replace("\r\n", "") # remove the enter 
        buyer_phone_number =list_from_amzon[9]
        buyer_email =list_from_amzon[7]
        buyer_name =list_from_amzon[8]
        sku=list_from_amzon[10]
        order_id=list_from_amzon[0]
        dpd_reference = sku_dpd_reference_pairs.get(sku, "Not Find. please check photo with this amazon_order_id = {}".format(order_id))
        product_name = list_from_amzon[11]
        # print(dpd_reference)
        # print(product_name)
        # print(recipient_name)
        # print(ship_address_1)
        # print(ship_postal_code)
        # print(ship_city)
        # print(ship_country)
        # print(buyer_phone_number)
        # print(buyer_email)

        name = recipient_name#"Denis Potemin-2"
        Firm = " " #if(hasNumbers(ship_address_1)) else ship_address_1 # if the address do not have number, then it is the company.
        strasse = (ship_address_1+" "+ship_address_2+" "+ship_address_3) #if(hasNumbers(ship_address_1)) else (ship_address_2+" "+ship_address_3)
        PLZ = ship_postal_code #"95336"
        Ort = ship_city #"Mainleus"
        Land = ship_country#"DEU"
        Telefon=buyer_phone_number #"015226395381019-Basic9"
        E_Mail= buyer_email #"fischenundmehr@gmail.com"
        KundenNr = order_id  # before it is the `buyer_name` ,now it is the Referenz 2: in the 面单.
        Referenz = dpd_reference #this is the Referenz 1: in the 面单.
        Inhalt = product_name
        Versanddatum =now.strftime("%d.%m.%Y  %H:%M:%S")
        if(sku =="1013"):  #1013	046+021	(这个需要两个面单,同一个人两个货)
            dataFirstLine = "Status;0;0;1;DPD;;{};{};{};;{};{};{};{};{};{};{};{};0,00;0,00;{};01.01.2000 00:00:00;01.01.2000 00:00:00;   \n".format(Firm, name, strasse, PLZ, Ort,Land,Telefon,E_Mail, KundenNr, Referenz, Inhalt, Versanddatum)
            pdp_file.write(dataFirstLine)
            dataFirstLine = "Status;0;0;1;DPD;;{};{};{};;{};{};{};{};{};{};{};{};0,00;0,00;{};01.01.2000 00:00:00;01.01.2000 00:00:00;   \n".format(Firm,name, strasse, PLZ, Ort,Land,Telefon,E_Mail, KundenNr, Referenz, Inhalt, Versanddatum)
            pdp_file.write(dataFirstLine)
        else:   
            dataFirstLine = "Status;0;0;1;DPD;;{};{};{};;{};{};{};{};{};{};{};{};0,00;0,00;{};01.01.2000 00:00:00;01.01.2000 00:00:00;  \n".format(Firm, name, strasse, PLZ, Ort,Land,Telefon,E_Mail, KundenNr, Referenz, Inhalt, Versanddatum)
            pdp_file.write(dataFirstLine)

file_stream.close()
pdp_file.close()