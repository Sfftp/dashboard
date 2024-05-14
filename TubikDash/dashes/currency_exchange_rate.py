import lxml.etree
import requests


def hui():
    # запрос к апи
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")

    # сохранение полученного XML-файла
    with open("currency_exchange_rate.xml", "w") as f:
        f.write(response.text)

    # парс XML-файла
    with open("currency_exchange_rate.xml") as fogj:
        xml = fogj.read()

    # смена кодировки на корректную
    xml = xml.encode("windows-1251")

    # получение тегов
    root = lxml.etree.fromstring(xml)

    # поиск необходимых данных
    required_valutes = {}
    for valute in root.getchildren():
        if valute[0].text in ["826", "784", "840", "978", "156", "949", "392"]:
            required_data = []
            codechar = ""
            for attribute in valute.getchildren():
                if attribute.tag == "CharCode":
                    codechar = attribute.text
                if attribute.tag in ["Name", "VunitRate"]:
                    required_data.append((attribute.tag, attribute.text))
                required_data_dict = {}
                for i in required_data:
                    required_data_dict[i[0]] = i[1]
                required_valutes[codechar] = required_data_dict

    # очистка пустых значений
    required_valutes = {k: v for k, v in required_valutes.items() if k}
    return required_valutes


