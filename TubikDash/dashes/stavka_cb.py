import lxml.etree
import requests
import csv

response = requests.get(
    "https://www.cbr.ru/hd_base/KeyRate/?UniDbQuery.Posted=True&UniDbQuery.From=17.09.2013&UniDbQuery.To=02.03.2024")

with open("../../data/stavka_cb.html", "w", encoding="utf8") as f:
    f.write(response.text)

with open("../../data/stavka_cb.html", encoding="utf8") as fogj:
    html = fogj.read()

parser = lxml.etree.HTMLParser()
html_root = lxml.etree.fromstring(html, parser)
n = html_root.getchildren()[1].getchildren()
data_cb = []

for i in html_root.findall(".//tr"):
    for j in i.getchildren():
        data_cb.append(j.text)

response_usd = requests.get(
    "http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=17/09/2013&date_req2=02/03/2024&VAL_NM_RQ=R01235")

with open("../../data/usd_data.xml", "w") as f:
    f.write(response_usd.text)

with open("../../data/usd_data.xml") as fogj:
    xml = fogj.read()

xml = xml.encode("windows-1251")
xml_root = lxml.etree.fromstring(xml)
usd_data = {}
for i in xml_root.findall(".//Record"):
    for j in i.getchildren():
        if j.tag == "VunitRate":
            usd_data[i.attrib["Date"]] = j.text

response_euro = requests.get(
    "http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=17/09/2013&date_req2=02/03/2024&VAL_NM_RQ=R01239")

with open("../../data/euro_data.xml", "w") as f:
    f.write(response_euro.text)

with open("../../data/euro_data.xml") as fogj:
    xml = fogj.read()

xml = xml.encode("windows-1251")
xml_root = lxml.etree.fromstring(xml)
euro_data = {}
for i in xml_root.findall(".//Record"):
    for j in i.getchildren():
        if j.tag == "VunitRate":
            euro_data[i.attrib["Date"]] = j.text

delimetr = 0
res = {}
temp = []
dates = []
cv = []

for i in range(len(data_cb)):
    if i % 2 == 0:
        dates.append(data_cb[i])
    else:
        cv.append(data_cb[i])

cv.remove("Ставка")
dates.remove("Дата")

for i in range(len(dates)):
    try:
        c = cv[i]
        usd = usd_data[dates[i]]
        euro = euro_data[dates[i]]
        res[dates[i]] = [c.replace(",", "."), usd.replace(",", "."), euro.replace(",", ".")]
    except KeyError:
        continue

for_csv = []
for i in res:
    temp = [i]
    for j in res[i]:
        temp.append(j)
    for_csv.append(temp)

for i in for_csv:
    date = i[0]
    day, month, year = date.split(".")
    i[0] = f"{year}-{month}-{day}"

for_csv = for_csv[::-1]
for_csv.insert(0, ["Date", "Rate", "Dollar", "Euro"])

for i in for_csv:
    i[0] = i[0].replace(".", "-")

with open('../../data/stavka_cb.csv', 'w', newline='', encoding="utf8") as ft:
    csv.writer(ft, delimiter=';').writerows(for_csv)
