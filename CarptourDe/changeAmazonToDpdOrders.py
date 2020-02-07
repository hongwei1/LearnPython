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
    "1013":"046+021",
    "2X-KD4H-M022":"BiteAlarm 4+1+Sw",
    "1038-Classic":"059NEW+DLeg",
    "1038-Comfort":"270001",
    "1037-Comfort":"059AD",
    "1027":"160019camo",
    "1039-Schwarz":"Rolle4000Black",
    "1044-Comfort 746523": "",
    "1005":"270013",
    "1019-Basic":"700016",#"Six bait boxes",
    "1019-Pro":"302011",#"Six bait boxes + Bag",
    "1022":" ",
    "AP-978G-XXFK":"270005",
    "1042-009":" ",
    "1020-5S":" ",
    "1020-5S":" ",
    "1034":"270038",
    "1031-235":" ",
    "1026-Pro":"1199 € Boat",
    "C9-KRTX-RO2C":"270025",
    "YS-RMGJ-0IZT":"270025",
    "1041-R1":"One-Wheel-Trolley",
    "1014":"Two-Wheel-Trolley",
    "1003":"160011"
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