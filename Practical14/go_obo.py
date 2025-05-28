# Project plan:
# 1. The purpose of the program is to parse a Gene Ontology (GO) XML file and find the deepest terms in three main ontologies: molecular_function, biological_process, and cellular_component.
# 2. The program will read the XML file, parse it, and extract terms along with their depth in the ontology hierarchy.
# 3. It will identify the deepest term for each ontology based on the number of 'is_a' relationships.
# 4. The results will be printed to the console, showing the term ID, name, and depth for each ontology.
# This program parses a Gene Ontology (GO) XML file to find the deepest terms in three main ontologies: molecular_function, biological_process, and cellular_component.
# The program uses two different XML parsing methods: DOM and SAX, and compares their performance.

# DOM method
# Import necessary libraries
import xml.dom.minidom
from datetime import datetime

def dom_parser(xml_file):
    start_time = datetime.now()
    
    # Parse the XML file
    dom = xml.dom.minidom.parse(xml_file)
    
    # Initialize dictionaries to store deepest terms for each ontology
    deepest_terms = {
        'molecular_function': {'id': None, 'name': None, 'depth': -1},
        'biological_process': {'id': None, 'name': None, 'depth': -1},
        'cellular_component': {'id': None, 'name': None, 'depth': -1}
    }
    
    # Get all term elements
    terms = dom.getElementsByTagName('term')
    
    for term in terms:
        # Get namespace (ontology)
        namespace = term.getElementsByTagName('namespace')[0].firstChild.data
        
        # Only process the three main ontologies
        if namespace not in deepest_terms:
            continue
            
        # Count is_a elements
        is_a_elements = term.getElementsByTagName('is_a')
        depth = is_a_elements.length
        
        # Get term id and name
        term_id = term.getElementsByTagName('id')[0].firstChild.data
        term_name = term.getElementsByTagName('name')[0].firstChild.data
        
        # Update if this term is deeper than current record
        if depth > deepest_terms[namespace]['depth']:
            deepest_terms[namespace]['id'] = term_id
            deepest_terms[namespace]['name'] = term_name
            deepest_terms[namespace]['depth'] = depth
    
    end_time = datetime.now()
    print(f"DOM Processing Time: {end_time - start_time}")
    return deepest_terms

if __name__ == "__main__":
    xml_file = r"c:\Users\HUAWEI\Desktop\IBI\IBI1_2024-25\Practical14\go_obo.xml"
    print("Running DOM parser...")
    dom_results = dom_parser(xml_file)
    print("DOM Results:")
    for ontology, data in dom_results.items():
        print(f"{ontology}: {data['id']} - {data['name']} (Depth: {data['depth']})")

# SAX method
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
    
    # Open the XML file
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