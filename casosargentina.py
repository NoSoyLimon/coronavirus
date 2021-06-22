from requests_html import HTMLSession
from datetime import datetime

week_days=["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]
week_num=(datetime.date(datetime.now())). weekday()

s = HTMLSession()
url = 'https://coronavirus.msal.gov.ar/publico/d/20as/sala-de-situacion-coronavirus-acceso-publico/d/20as/sala-de-situacion-coronavirus-acceso-publico'

r = s.get(url)

r.html.render(sleep=7)

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
bloque6 = r.html.xpath('//*[@id="panel-101"]', first=True)
casos_activos = bloque6.text.replace("Total Activos\n","")
bloque7= r.html.xpath('//*[@id="panel-100"]', first=True)
total_recuperados = bloque7.text.replace("Total recuperados\n","")
bloque8 = r.html.xpath('//*[@id="panel-107"]', first=True)
internados = bloque8.text.replace("Confirmados Covid internados UTI\n","")
bloque9 = r.html.xpath('//*[@id="panel-108"]/div/div/div[1]/div/div[2]/div/plugin-component/panel-plugin-singlestat/grafana-panel/ng-transclude/div/div/span[1]/span', first=True)
uti_pais = bloque9.text.replace(".",",")
bloque10 = r.html.xpath('//*[@id="panel-109"]/div/div/div[1]/div/div[2]/div/plugin-component/panel-plugin-singlestat/grafana-panel/ng-transclude/div/div/span[1]/span', first=True)
uti_amba = bloque10.text.replace(".",",")

nuevos_casos = ('{:,}'.format(int(nuevos_casos)).replace(',','.'))
nuevos_muertos = ('{:,}'.format(int(nuevos_muertos)).replace(',','.'))
total_casos = ('{:,}'.format(int(total_casos)).replace(',','.'))
total_muertos = ('{:,}'.format(int(total_muertos)).replace(',','.'))
testeos = ('{:,}'.format(int(testeos)).replace(',','.'))
casos_activos = ('{:,}'.format(int(casos_activos)).replace(',','.'))
total_recuperados = ('{:,}'.format(int(total_recuperados)).replace(',','.'))
internados = ('{:,}'.format(int(internados)).replace(',','.'))


print('TÍTULO: Coronavirus en Argentina:', nuevos_casos, 'nuevos casos y', nuevos_muertos, 'muertos')
print('BAJADA: Desde que inició la pandemia, el país ya registró', total_casos, 'contagios de COVID 19.')
print('El Ministerio de Salud de la Nación reportó este',week_days[week_num] , nuevos_casos,  'nuevos casos de coronavirus y', nuevos_muertos, 'fallecidos.')
print('A partir de estos datos, el país ya registró', total_casos, 'contagios y', total_muertos, 'víctimas fatales desde el inicio de la pandemia.')
print("En las últimas 24 horas se realizaron", testeos, "testeos, con una positividad del", positividad + "%.")
print('Actualmente se registran', casos_activos, 'casos positivos activos en todo el país y', total_recuperados, 'pacientes recuperados.')
print('El reporte indica que son', internados, 'los pacientes internados en unidades de terapia intensiva, con un porcentaje de ocupación de camas de adultos de', uti_pais, 'en el país y del', uti_amba, 'en el Área Metropolitana de Buenos Aires (AMBA).')