from xml.etree.ElementTree import parse

tree = parse(r"markup_lang\note.xml")
note = tree.getroot()

print(note.get("date"))
for parent in tree.iter():
    for child in parent:
        print(child.text)