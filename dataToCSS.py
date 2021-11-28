import json

    # load existing package.json file, parse JSON and save height and width
    # it's really important when it comes to rendering certain amoung of divs in cols and rows
with open("package.json", encoding='utf-8', errors='ignore') as json_data:
     data = json.load(json_data, strict=False)

WIDTH = int(data['width'])              # assign WIDTH nad HEIGHT values
HEIGHT = int(data['height'])
HTML_FILENAME = 'test.html'             # customize html filename
PIXEL_SCALE = 1


html_file = open(HTML_FILENAME, 'w')

def generateStyles(data):
    """Generate <style> tag with classes for every <div>."""
    html_file.write('<style>')          # create <style> tag
                                        # write styles to file
    html_file.write('.flexDiv{display: flex;}\n')
    image_data = data['imageData']              # assign image data to a variable to simpify usage
    image_data_length = len(data['imageData'])  # sameeee bro lol
    for i in range(image_data_length):          # ik you could just multiply HEIGHT and WIDTH but it's much cooler B)
        html_file.write(f'.pixel{i}')
        html_file.write('{background: '+ image_data[i]+f'; width: {PIXEL_SCALE}px; height: {PIXEL_SCALE}px;'+'}\n')


        
    html_file.write('</style>')        # close </style> tag
    html_file.write('</head>')         # close </head> tag
    pass

def generateDivs(data):
    """Generate divs as cols and rows in existing HTML file."""

    pixel_iterate = 0                   # a variable that stores our pixel number (simple helper)
    html_file.write('<body>')           # open <body> tag

                                        # generate <div> tag with a class name
    for i in range(HEIGHT):
        html_file.write('<div class="flexDiv">\n')
        for j in range(WIDTH):
            html_file.write(f'<div class="pixel{pixel_iterate}"></div>\n')
            pixel_iterate += 1

        html_file.write('</div>\n')
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




