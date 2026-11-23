import xml.etree.ElementTree as ET;

class XMLReader:
    CUBE_TAG = "{http://www.ecb.int/vocabulary/2002-08-01/eurofxref}Cube";

    def __init__(self):
        pass;

    def read(self, file_path="currencies.xml"):
        root = ET.parse(file_path).getroot();

        return {cube.attrib["currency"]: cube.attrib["rate"] for cube in root.iter(self.CUBE_TAG) if "currency" in cube.attrib and "rate" in cube.attrib};