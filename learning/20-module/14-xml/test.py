#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/8 15:51
@Description: 

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/8 15:51
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

import xml.etree.ElementTree as ET

tree = ET.parse("test.xml")
root = tree.getroot()
print(root.tag)

# 遍历xml文档
for child in root:
    print(child.tag, child.attrib)

    for i in child:
        print(i.tag, i.text)

# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)

# 修改
for node in root.iter('year'):
    node.text = str(int(node.text) + 1)
    node.set("updated", "yes")

tree.write("test_update.xml")

# 删除node
for country in root.findall('country'):
    if int(country.find('rank').text) > 50:
        root.remove(country)

tree.write('test_remove.xml')

# 创建xml文档
new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
age = ET.SubElement(name, "age", attrib={"checked": "no"})
sex = ET.SubElement(name, "sex")
sex.text = '33'

name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
age2 = ET.SubElement(name2, "age")
age2.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test_create.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式