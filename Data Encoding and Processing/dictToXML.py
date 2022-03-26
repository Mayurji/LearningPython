from xml.etree.ElementTree import Element

def dict_to_xml(tag, d):
    elem = Element(tag)
    for k, v in d.items():
        child = Element(k)
        child.text = str(v)
        elem.append(child)
    return elem

s = {'name': 'GOOG', 'shares': 100, 'price':490.1 }
e = dict_to_xml('stock', s)
print(f'Dict To XML: {e.findtext("name")}')