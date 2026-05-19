import xml.dom.minidom
import xml.sax
from datetime import datetime
import zipfile

# The <is_a> tag represents a hierarchical "is a type of" relationship between GO terms, 
# and its count indicates how specific (deep in the hierarchy) a term is.


def read_xml_from_zip(zip_path, xml_filename="go_obo.xml"):
    """
    Read XML file from a ZIP archive and return the file object
    :param zip_path: Path to the ZIP file (e.g., "go_obo.xml.zip")
    :param xml_filename: Name of the XML file inside the ZIP archive
    :return: Binary stream of the XML file (directly usable by XML parsers)
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Check if the target file exists in the ZIP archive
        if xml_filename not in zip_ref.namelist():
            raise FileNotFoundError(f"File not found in ZIP: {xml_filename}")
        # Read the XML file content and return the file object
        xml_file = zip_ref.open(xml_filename)
        return xml_file
        
# -------------------------- DOM Parsing Function --------------------------
def dom_analysis(xml_file):
    """DOM parsing: Find the GO term with the maximum <is_a> count in each ontology"""
    start_time = datetime.now()

    # Initialize statistics for the three GO ontologies (term name, max is_a count)
    go_stats = {
        "molecular_function": {"name": "", "max_is_a": 0},
        "biological_process": {"name": "", "max_is_a": 0},
        "cellular_component": {"name": "", "max_is_a": 0}
    }

    # Parse the entire XML file into a DOM tree
    dom_tree = xml.dom.minidom.parse(xml_file)
    terms = dom_tree.getElementsByTagName("term")

    for term in terms:
        # Extract the namespace (ontology type)
        namespace_ele = term.getElementsByTagName("namespace")[0]
        namespace = namespace_ele.firstChild.data.strip()

        # Skip terms that do not belong to the three main ontologies
        if namespace not in go_stats:
            continue

        # Extract the human-readable name of the GO term
        name_ele = term.getElementsByTagName("name")[0]
        term_name = name_ele.firstChild.data.strip()

        # Count the number of <is_a> relationships for this term
        is_a_list = term.getElementsByTagName("is_a")
        is_a_count = len(is_a_list)

        # Update the maximum value for the corresponding ontology
        if is_a_count > go_stats[namespace]["max_is_a"]:
            go_stats[namespace]["name"] = term_name
            go_stats[namespace]["max_is_a"] = is_a_count

    # Calculate total execution time
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    return go_stats, duration

# -------------------------- SAX Parser Class & Function --------------------------
class GOContentHandler(xml.sax.ContentHandler):
    """SAX custom handler: Parse XML line-by-line in a streaming fashion"""
    def __init__(self):
        # Initialize statistics for the three GO ontologies
        self.go_stats = {
            "molecular_function": {"name": "", "max_is_a": 0},
            "biological_process": {"name": "", "max_is_a": 0},
            "cellular_component": {"name": "", "max_is_a": 0}
        }
        # Temporary variables to store data of the current term being parsed
        self.current_tag = ""
        self.current_namespace = ""
        self.current_name = ""
        self.current_is_a_count = 0

    # Triggered when a new XML tag is encountered
    def startElement(self, name, attrs):
        self.current_tag = name
        if name == "term":
            # Reset temporary variables for a new GO term
            self.current_namespace = ""
            self.current_name = ""
            self.current_is_a_count = 0

    # Collect text content inside XML tags
    def characters(self, content):
        if self.current_tag == "namespace":
            self.current_namespace += content.strip()
        elif self.current_tag == "name":
            # Concatenate name text 
            self.current_name += content.strip()

    # Triggered when the closing tag of an element is encountered
    def endElement(self, name):
        if name == "is_a":
            # Increment count for each <is_a> relationship
            self.current_is_a_count += 1
        elif name == "term":
            # Finalize parsing for one term and update the statistics
            ns = self.current_namespace
            if ns in self.go_stats:
                if self.current_is_a_count > self.go_stats[ns]["max_is_a"]:
                    self.go_stats[ns]["name"] = self.current_name
                    self.go_stats[ns]["max_is_a"] = self.current_is_a_count
        self.current_tag = ""

def sax_analysis(xml_file):
    """SAX parsing: Execute the custom content handler"""
    start_time = datetime.now()

    # Create and configure the SAX parser
    parser = xml.sax.make_parser()
    handler = GOContentHandler()
    parser.setContentHandler(handler)
    parser.parse(xml_file)

    # Calculate total execution time
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    return handler.go_stats, duration

# -------------------------- Main Program: Run and Print Results --------------------------
if __name__ == "__main__":
    ZIP_PATH = "go_obo.xml.zip"

    # DOM analysis
    print("="*60)
    print("DOM Parsing Results")
    print("="*60)
    with read_xml_from_zip(ZIP_PATH) as xml_file_dom:
        dom_results, dom_time = dom_analysis(xml_file_dom)
    for ns, info in dom_results.items():
        print(f"Ontology: {ns}")
        print(f"  Term Name: {info['name']}")
        print(f"  Max <is_a> Count: {info['max_is_a']}\n")
    print(f"DOM Execution Time: {dom_time:.4f} seconds\n")

    # SAX analysis
    print("="*60)
    print("SAX Parsing Results")
    print("="*60)
    with read_xml_from_zip(ZIP_PATH) as xml_file_sax:
        sax_results, sax_time = sax_analysis(xml_file_sax)
    for ns, info in sax_results.items():
        print(f"Ontology: {ns}")
        print(f"  Term Name: {info['name']}")
        print(f"  Max <is_a> Count: {info['max_is_a']}\n")
    print(f"SAX Execution Time: {sax_time:.4f} seconds\n")

    # Performance comparison comment 
    if sax_time < dom_time:
        print("# SAX runs faster than DOM")
    else:
        print("# DOM runs faster than SAX")