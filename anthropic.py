from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from PyPDF2 import PdfReader
import re

# Read in the PDF file
reader = PdfReader('./ciayn.pdf')

# printing number of pages in pdf file
print(len(reader.pages))

pages = reader.pages
pdftext=""

# Extract text from the PDF
for page in pages:
    pdftext += page.extract_text()

# Write text to output file if necessary
import io

file ='./ciayn.txt'
#with io.open(file, 'w') as f:
#  f.write(pdftext)

# print whole text for debugging
# print(pdftext)

# Resolve encoding issues
#pdftext = pdftext.encode('utf-8')
#pdftext = re.sub(r'\\ud835.+?', '', pdftext)
#pdftext = re.sub(r'\\u,+?', '', pdftext)

print("# of words: " + str(len(pdftext.split())))

anthropic = Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=<anthropic_api_key>,
)

completion = anthropic.completions.create(
    model="claude-2",
    max_tokens_to_sample=100000,
#    prompt=f"{HUMAN_PROMPT} Summarize the main points of the paper here https://arxiv.org/abs/2307.06962 and give me the top five reference papers. For each of the reference papers, write me sample code that represents the main point of the paper.{AI_PROMPT}",
    prompt=f"{HUMAN_PROMPT} Summarize the main points of the paper delineated by '?????'.  Give me the top five reference papers. For each of the reference papers, write me full executable sample code that represents the main point of the paper.  ????? " + pdftext + "?????" + f"{AI_PROMPT}",
)
print(completion.completion)
