# the docs for the format:  https://docs.google.com/spreadsheets/d/1LGEnOfUu5PjuE42dMoEhIRve5rv3vNsBtk-8DWozwdg/edit?ts=5e322488#gid=870428257
import codecs
from datetime import datetime
now = datetime.now() # current date and time


# Referenz ==> Amazon.product-name:
#     if ("Heigh") ==> "CarpOn Stuhl extra Heigh Camping Einstellbar Carp Fishing Chair 130kg" =="270025"
#     if("XXL" and "8" ) ==>"CarpOn Liege 8 Camping- Beine XXL Karpfenliege" =="270005"

#Inhalt ==>Amazon.product-name:


file_location = "19959998464018295.txt"

file_stream = codecs.open(file_location, 'r', 'utf-8')
file_output = codecs.open("19959998464018295.csv", 'w', 'utf-16')
dpdFirstLine = "Action;ItemID;TransactionID;ShippingStatus;ShippingCarrierUsed;ShipmentTrackingNumber;Firma;Name;Strasse;Adresszusatz;PLZ;Ort;Land;Telefon;E-Mail;KundenNr;Referenz;Inhalt;Gewicht;Nachnahmebetrag;Versanddatum;StatusdatumAbgeholt;StatusdatumZugestellt;PaketstatusID \n"
file_output.write(dpdFirstLine)


i = 0
for l in file_stream:
    i=i+1
    if (i==1): # not need the first line
        None
    else:
        list123 = l.split("\t")
        recipient_name = list123[16]
        ship_address_1 = list123[17]
        ship_address_2 = list123[18]
        ship_address_3 = list123[19]
        ship_postal_code =list123[22]
        ship_city =list123[20]
        ship_country =list123[23].replace("\r\n","") # remove the enter 
        buyer_phone_number =list123[9]
        buyer_email =list123[7]
        print(recipient_name)
        print(ship_address_1)
        print(ship_postal_code)
        print(ship_city)
        print(ship_country)
        print(buyer_phone_number)
        print(buyer_email)

        name = recipient_name#"Denis Potemin-2"
        strasse = ship_address_1+" "+ship_address_2+" "+ship_address_3 #"Pölzer Str. 20 A"
        PLZ = ship_postal_code #"95336"
        Ort = ship_city #"Mainleus"
        Land = ship_country#"DEU"
        Telefon=buyer_phone_number #"015226395389"
        E_Mail= buyer_email #"fischenundmehr@gmail.com"
        KundenNr = "  "
        Referenz = "270005" # can not find it from Amazon.
        Inhalt = "8-Beine XXL" # can not find it from Amazon.
        Versanddatum =now.strftime("%d.%m.%Y  %H:%M:%S") #"30.01.2020 00:00:00" # today time? 
        dataFirstLine = "Status;0;0;1;DPD;  ;;{};{};;{};{};{};{};{};{};{};8-Beine XXL;0,00;0,00;{};01.01.2000 00:00:00;01.01.2000 00:00:00;   \n".format(name, strasse, PLZ, Ort,Land,Telefon,E_Mail, KundenNr, Referenz, Inhalt, Versanddatum)
        file_output.write(dataFirstLine)

file_stream.close()
file_output.close()