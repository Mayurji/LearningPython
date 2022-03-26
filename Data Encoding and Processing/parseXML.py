from xml.etree.ElementTree import parse

xml = open('book.xml')
doc = parse(xml)
item = doc.find('channel/title')
print(f"Book's parameter: {item.text}")