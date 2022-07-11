#!/usr/bin/env python3

import shutil
import sys
import os
import json

def get_city_by_id(city_id):

    cities = { "1": "Adana", 
         "2"   : "Adıyaman",     
         "3"   : "Afyon",        
         "4"   : "Ağrı",         
         "5"   : "Amasya",
         "6"   : "Ankara",       
         "7"   : "Antalya",      
         "8"   : "Artvin",       
         "9"   : "Aydın",        
        "10"   : "Balıkesir",
        "11"   : "Bilecik",      
        "12"   : "Bingöl",       
        "13"   : "Bitlis",       
        "14"   : "Bolu",         
        "15"   : "Burdur",
        "16"   : "Bursa",        
        "17"   : "Çanakkale",	
        "18"   : "Çankırı",      
        "19"   : "Çorum",        
        "20"   : "Denizli",
        "21"   : "Diyarbakır",	
        "22"   : "Edirne",       
        "23"   : "Elazığ",       
        "24"   : "Erzincan",     
        "25"   : "Erzurum",
        "26"   : "Eskişehir",	
        "27"   : "Gaziantep",	
        "28"   : "Giresun",      
        "29"   : "Gümüşhane",
        "30"   : "Hakkari",
        "31"   : "Hatay",
        "32"   : "Isparta",
        "33"   : "Mersin",
        "34"   : "İstanbul",
        "35"   : "İzmir",
        "36"   : "Kars",         
        "37"   : "Kastamonu",
        "38"   : "Kayseri",      
        "39"   : "Kırklareli",	
        "40"   : "Kırşehir",
        "41"   : "Kocaeli",      
        "42"   : "Konya",        
        "43"   : "Kütahya",      
        "44"   : "Malatya",      
        "45"   : "Manisa",
        "46"   : "Kahramanmaraş",      
        "47"   : "Mardin",       
        "48"   : "Muğla",        
        "49"   : "Muş",          
        "50"   : "Nevşehir",
        "51"   : "Niğde",        
        "52"   : "Ordu",         
        "53"   : "Rize",         
        "54"   : "Sakarya",      
        "55"   : "Samsun",
        "56"   : "Siirt",        
        "57"   : "Sinop",        
        "58"   : "Sivas",        
        "59"   : "Tekirdağ",     
        "60"   : "Tokat",
        "61"   : "Trabzon",      
        "62"   : "Tunceli",      
        "63"   : "Şanlıurfa",	
        "64"   : "Uşak",         
        "65"   : "Van",
        "66"   : "Yozgat",       
        "67"   : "Zonguldak",	
        "68"   : "Aksaray",      
        "69"   : "Bayburt",      
        "70"   : "Karaman",
        "71"   : "Kırıkkale",	
        "72"   : "Batman",       
        "73"   : "Şırnak",       
        "74"   : "Bartın",       
        "75"   : "Ardahan",
        "76"   : "Iğdır",        
        "77"   : "Yalova",       
        "78"   : "Karabük",      
        "79"   : "Kilis",        
        "80"   : "Osmaniye",
        "81"   : "Düzce",
        "96"   : "Kıbrıs",
        "2622" : "Kıbrıs",
        "2623" : "Kıbrıs",
        "2624" : "Kıbrıs",
        "2625" : "Kıbrıs",
        "2626" : "Kıbrıs"
    }

    return cities[str(city_id)]

def main(path):
    for json_file in os.scandir(path):
        if(json_file.is_file() & (json_file.name[-4:] == "json")):
            data = json.load(open(json_file.name))
            city_name = get_city_by_id(data["cityId"])
            os.makedirs(city_name, exist_ok=True)
            quarter_name = data["name"].replace(" ","-")
            full_path = city_name + "/" + quarter_name + ".json"
            shutil.copyfile(json_file.name,full_path) 
            os.remove(json_file.name)

    sys.stdout.write("--- done ---")

if __name__ == "__main__":
    main(".")
