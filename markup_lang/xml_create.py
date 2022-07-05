#	XML 문서를 만들려면? ― xml.etree.ElementTree
from xml.etree.ElementTree import Element, dump, SubElement

note = Element("note")
to = Element("to")
to.text = "Tove"

note.append(to)
SubElement(note, "from").text = "Jani"	# 태그 추가
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!"
note.attrib["date"] = "20220705"  		# 속성 추가
dump(note)  # note 엘리먼트를 XML로 출력

#	XML 보기좋게 만들어 저장
from xml.dom import minidom
import xml.etree.ElementTree as ET
xmlstr = minidom.parseString(ET.tostring(note)).toprettyxml(indent="  ")
print(xmlstr)

# XML을 파일로 저장
with open(r'markup_lang\noteResult.xml', 'w') as f:
    f.write(xmlstr)