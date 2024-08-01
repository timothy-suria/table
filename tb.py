import csv
import html

# Read the CSV file
with open('c:\Monash\Table_Input.csv', 'r') as file:
    reader = csv.reader(file)
    # Skip the header
    next(reader, None)
    # Start the HTML table
    html_output = '<table border="1">\n'
    html_output += '    <tr>\n        <th>Index</th>\n        <th>Value</th>\n    </tr>\n'
    # Add rows to the HTML table
    for row in reader:
        index, value = row
        html_output += f'    <tr>\n        <td>{html.escape(index)}</td>\n        <td>{html.escape(value)}</td>\n    </tr>\n'
    # Close the HTML table
    html_output += '</table>'

# Write the HTML output to a file
with open('output.html', 'w') as file:
    file.write(html_output)
