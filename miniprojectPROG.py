# deel Muridi Aboukar

from tkinter import *
import requests
import xmltodict

#returnt een lijst met alle vertrektijden als strings
def vertrekTijd(code):
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + code
    response = requests.get(api_url, auth=inlogGegevens)
    vertrekXML = xmltodict.parse(response.text)
    vertrekList = []
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        str = vertrek['EindBestemming'] + ';'
        str += vertrek['VertrekTijd'][11:16] + ';'
        str += vertrek['TreinSoort'] + ';'
        #er is niet altijd een spoor bekend bij het XML bestand van de NS. daarom gebruiken we hier een try/except
        try:
            str += vertrek['VertrekSpoor']['#text']
        except:
            str += 'onbekend'
        vertrekList.append(str)
    return vertrekList

#returnt een lijst met alle vertrektijden als strings
def storingen(code):
    api_url = 'http://webservices.ns.nl/ns-api-storingen?station=' + code
    response = requests.get(api_url, auth=inlogGegevens)
    storingXML = xmltodict.parse(response.text)
    storingList = []
    if storingXML['Storingen']['Gepland'] != None:
        storingList.append('Werkzaamheden')
        if type(storingXML['Storingen']['Gepland']['Storing']) == list:
            for storing in storingXML['Storingen']['Gepland']['Storing']:
                storingList.append(storing['Traject'] + ' ' + storing['Periode'])
        else:
            storingList.append(storingXML['Storingen']['Gepland']['Storing']['Traject'] + ' ' + storingXML['Storingen']['Gepland']['Storing']['Periode'])

    if storingXML['Storingen']['Ongepland'] != None:
        storingList.append('')
        storingList.append('Ongeplande storingen')
        if type(storingXML['Storingen']['Ongepland']['Storing']) == list:
            x = storingXML['Storingen']['Ongepland']['Storing'][0]
            storingList.append(x['Traject'] + ' ' + x['Reden'])
        else:
            x = storingXML['Storingen']['Ongepland']['Storing']
            storingList.append(x['Traject'] + ' ' + x['Reden'])

    return storingList