import os, PyPDF2
from gtts import gTTS
from tkinter import Tk
from tkinter.filedialog import askopenfilename


window = Tk()
window.withdraw()

file = askopenfilename(filetypes=[('pdf file', '*.pdf')])

pdf = open(file, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdf)
number_of_pages = pdfReader.numPages

strings = []
full_text = ""

for page_number in range(0, number_of_pages):
    page = pdfReader.getPage(page_number)
    text = page.extractText()
    full_text += text

language = "en"

file_name = os.path.basename(file)
new_file_name = os.path.splitext(file_name)

test = gTTS(text=full_text, lang=language, slow=False)
test.save(f"{new_file_name[0]}.mp3")
