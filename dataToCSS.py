import json

    # load existing package.json file, parse JSON and save height and width
    # it's really important when it comes to rendering certain amoung of divs in cols and rows
with open("package.json", encoding='utf-8', errors='ignore') as json_data:
     data = json.load(json_data, strict=False)

WIDTH = int(data['width'])              # assign WIDTH nad HEIGHT values
HEIGHT = int(data['height'])
HTML_FILENAME = 'test.html'             # customize html filename

html_file = open(HTML_FILENAME, 'w')

def generateStyles(data):
    """Generate <style> tag with classes for every <div>."""
    html_file.write('</head>')         # close head tag
    pass

def generateDivs(data):
    """Generate divs as cols and rows in existing HTML file."""
    html_file.write('<body>')           # open <body> tag

                                        # write styles to file
    # for i in range(data['obraz']):  
    print(len(data['imageData']))     
        



    html_file.write("""
        </body>
    </html> 
        """)                            # close </body> and </html> tag
    pass

def createHTMLStruct(data):
    """Create simple HTML file structure with tags."""
    
    begin_structure = """
    <html>
    <head>
        <title>Generated</title>
    """
    html_file.write(begin_structure)    # start HTML structure
    generateStyles(data)                # generate styles tag and close </head> tag
    generateDivs(data)                  # create <body></body> tag and writes div with classes into them

                 


createHTMLStruct(data)

html_file.close()    # close the file




