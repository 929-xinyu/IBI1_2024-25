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