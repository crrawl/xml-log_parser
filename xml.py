import re

xml = "AudioSFX.xml"
outFile = "output.txt"

# Open and read
with open(xml, "r") as xml:
    xmlContent = xml.read()

# Find by regex pattern
pattern = r'<File Id="(\d+)".*?<Path>(.*?)</Path>'
matches = re.findall(pattern, xmlContent, re.DOTALL)

# Open and write
with open(outFile, "w") as out_file:
    out_file.write("id:path\n")
    for file_id, file_path in matches:
        out_file.write(f"{file_id}:{file_path}\n")

print(f"Rezultāts ierakstīts failā {outFile}")