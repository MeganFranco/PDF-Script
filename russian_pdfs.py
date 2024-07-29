import pdfplumber

file_name = input("Enter the file name: ")
print("You entered: " + file_name)

pdf = pdfplumber.open("[dir]/Python/pdfWork/" + file_name)


print("pages: ", len(pdf.pages))
num_pages = len(pdf.pages)

new_file = open(file_name.replace(' ', '')[:-4]  + ".txt", "w+")

for x in pdf.pages:
  text = x.extract_text()
  new_file.write(text.lower())
  print(text.lower())

new_file.close()
pdf.close()
