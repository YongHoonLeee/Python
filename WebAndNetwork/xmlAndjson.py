import xml.etree.ElementTree as ET


root = ET.Element('root')
tree = ET.ElementTree(element=root)
employee = ET.SubElement(root, 'employee')
employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '111'
employ_name = ET.SubElement(employ, 'name')
employ_name.text = 'Yonghoon'
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '222'
employ_name = ET.SubElement(employ, 'name')
employ_name.text = 'Nancy'

tree.write('./WebAndNetwork/test.xml', encoding='utf-8', xml_declaration=True)


"""

<?xml version='1.0' encoding = 'utf-8'?>
<root>
    <employee>
        <employ>
            <id>111</id>
            <name>Yonghoon</name>
        </employ>
        <employ>
            <id>222</id>
            <name>Nancy</name>
        </employ>
    </employee>
<root>

{
    "employee":
        [
            {"id": 111, "name": "Yonghoon"},
            {"id": 222, "name": "Nancy"}
        ]
}
"""
