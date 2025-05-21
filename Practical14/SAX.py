import xml.sax
from datetime import datetime

class GOTermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.current_term = {}
        self.deepest_terms = {
            'molecular_function': {'id': None, 'name': None, 'depth': -1},
            'biological_process': {'id': None, 'name': None, 'depth': -1},
            'cellular_component': {'id': None, 'name': None, 'depth': -1}
        }
        self.is_a_count = 0
        self.in_name = False
        self.in_namespace = False
        self.in_id = False
    
    def startElement(self, tag, attributes):
        self.current_data = tag
        if tag == 'term':
            self.current_term = {'id': '', 'name': '', 'namespace': '', 'is_a_count': 0}
        elif tag == 'is_a':
            self.current_term['is_a_count'] += 1

    def characters(self, content):
        if self.current_data == 'name':
            if 'name' in self.current_term:
                self.current_term['name'] += content
        elif self.current_data == 'namespace':
            if 'namespace' in self.current_term:
                self.current_term['namespace'] += content
        elif self.current_data == 'id':
            if 'id' in self.current_term:
                self.current_term['id'] += content
    
    def endElement(self, tag):
        if tag == 'term':
            namespace = self.current_term.get('namespace', '')
            if namespace in self.deepest_terms:
                current_depth = self.current_term.get('is_a_count', 0)
                if current_depth > self.deepest_terms[namespace]['depth']:
                    self.deepest_terms[namespace]['id'] = self.current_term.get('id')
                    self.deepest_terms[namespace]['name'] = self.current_term.get('name')
                    self.deepest_terms[namespace]['depth'] = current_depth
        self.current_data = ""

def sax_parser(xml_file):
    start_time = datetime.now()
    
    # Create a SAX parser
    parser = xml.sax.make_parser()
    # Turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    
    # Override the default ContextHandler
    handler = GOTermHandler()
    parser.setContentHandler(handler)
    
    # 修改为用 open 打开本地文件
    with open(xml_file, 'r', encoding='utf-8') as f:
        parser.parse(f)
    
    end_time = datetime.now()
    print(f"SAX Processing Time: {end_time - start_time}")
    return handler.deepest_terms

if __name__ == "__main__":
    xml_file = r"c:\Users\HUAWEI\Desktop\IBI\IBI1_2024-25\Practical14\go_obo.xml"
    print("\nRunning SAX parser...")
    sax_results = sax_parser(xml_file)
    print("SAX Results:")
    for ontology, data in sax_results.items():
        print(f"{ontology}: {data['id']} - {data['name']} (Depth: {data['depth']})")