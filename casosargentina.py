from requests_html import HTMLSession
from datetime import datetime

week_days=["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]
week_num=(datetime.date(datetime.now())). weekday()

s = HTMLSession()
url = 'https://coronavirus.msal.gov.ar/publico/d/20as/sala-de-situacion-coronavirus-acceso-publico/d/20as/sala-de-situacion-coronavirus-acceso-publico'

r = s.get(url)

r.html.render(sleep=10)

bloque1 = r.html.xpath('//*[@id="panel-48"]', first=True)
nuevos_casos = bloque1.text.replace("Confirmados del día\n","")
bloque2 = r.html.xpath('//*[@id="panel-99"]', first=True)
nuevos_muertos = bloque2.text.replace("Fallecidos del día\n","")
bloque3 = r.html.xpath('//*[@id="panel-98"]', first=True)
total_casos = bloque3.text.replace("Total Confirmados\n","")
bloque4 = r.html.xpath('//*[@id="panel-58"]', first=True)
total_muertos = bloque4.text.replace("Total Fallecidos\n","")
bloque5 = r.html.xpath('//*[@id="panel-102"]', first=True)
testeos = bloque5.text.replace("Testeos del día\n","")
positividad = (int(nuevos_casos)*100)/int(testeos)
positividad = round(positividad, 2)
positividad = str(positividad)


#Actualmente se registran casos_activos casos positivos activos en todo el país y total_recuparados pacientes recuperados.




print('El Ministerio de Salud de la Nación reportó este',week_days[week_num] , nuevos_casos,  'nuevos casos de coronavirus y', nuevos_muertos, 'fallecidos.')
print('A partir de estos datos, el país ya registró', total_casos, 'contagios y', total_muertos, 'víctimas fatales desde el inicio de la pandemia.')
print("En las últimas 24 horas se realizaron", testeos, "testeos, con una positividad del", positividad + "%.")
#print(f'El area es: {area:,.2f}')