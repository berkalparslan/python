bilgisayara python kurmak gerekiyor. eger kurulu degil ise 
windows icin : https://www.python.org/downloads/windows/

mac icin brew kurulu ise kolay yoldan terminalde: 
"brew install python"


daha sonra:
"pip3 install pyautogui"


daha sonra egitim.py'nin terminalden bulundugu klasore gidip:
"python3 egitim.py"

komutunu kosarsanız uygulama calısır, mouse'u hareket ettirdikce terminaldeki x-y kordinatları degisir;

findPosition fonksiyonu acık iken tıklamak istediginiz yerin konumunu bulup kaydetmeniz gerekiyor. 

daha sonra ctrl+c ile terminalde durdurup, 19.satırda kaydettiginiz konumu girmelisiniz ve alttaki fonksiyonları bu hale getirmelisiniz:

# findPosition()
click()


tekrar:
"python3 egitim.py" 
calıstırırsanız 15 snde bir o noktaya tıklayacaktır.

