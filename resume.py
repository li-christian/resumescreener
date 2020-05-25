# importing required modules
import PyPDF2
import re
import textract
import string

# replace name of pdf with yours
pdfFileObj = open('christian_li.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# number of pages in pdf file
num_pages = pdfReader.numPages
count = 0

#empy string variable
text = ""

# extracting the text of every page on the pdf
while count < num_pages:
    page = pdfReader.getPage(count)
    count += 1
    text += page.extractText()

# Convert all strings to lowercase
text = text.lower()

# Remove numbers
text = re.sub(r'\d+','',text)

# Remove punctuation
text = text.translate(str.maketrans('','',string.punctuation))

# NEW CODE - starts here, add terms accordingly to requirements

terms = {
        'Education' : ['bachelor', 'master', 'electrical engineering',' software engineering','mechanical engineering','civil engineering','chemical engineering',
                    'geomatics engineering', 'computer Science', 'mathematics', 'economics','computer engineering'],
        'Experience' : ['software developer intern', 'city operations representative', 'electrical engineering intern', 'food and beverage',
                        'mechanical engineering intern', 'chemical engineering intern', 'civil engineering intern', 'accounting intern', 'finance intern',
                        'electrical engineer', 'project manager', 'consultant', 'mechanical engineer', 'civil engineer','software engineer', 'software developer',
                        'data scientist', 'process engineer', 'supervisor', 'optimization engineer'],

        'Skills' : ['iot','internet','machine learning','analytics','api','aws','big data','busines intelligence','clustering','code',
                          'coding','data','database','data mining','data science','deep learning','hadoop',
                          'hypothesis test','modeling','nosql','nlp',
                          'predictive','text mining','programming','python','r','sql','tableau',
                          'visualuzation', 'matlab','html','css','salesforce','autocad', 'c', 'java','project management'],
        'Volunteer' : ['community','mentorship','mentor','mentee','events','leadership','industry', 'ieee'],
        'Certificates' : ['python', 'r', 'statistics', 'blockchain', 'black belt','six sigma','leadership','c',
                        'automation', 'production']
        }

#categorize
count = 0
Education = []
Experience = []
Skills = []
Volunteer = []
Certificates = []

#finding keywords in your resume and putting them into a list
#count increment based on subjective weighting
for area in terms.keys():
    if area == 'Education':
        for word in terms[area]:
            if word in text:
                Education.append(word)
                count += 1

    if area == 'Skills':
        for word in terms[area]:
            if word in text:
                Skills.append(word)
                count += 0.25

    if area == 'Experience':
        for word in terms[area]:
            if word in text:
                Experience.append(word)
                count += 1.5

    if area == 'Volunteer':
        for word in terms[area]:
            if word in text:
                Volunteer.append(word)
                count += 0.25

    if area == 'Certificates':
        for word in terms[area]:
            if word in text:
                Certificates.append(word)
                count += 0.25

print('Education: ',Education)
print('Experience: ',Experience)
print('Skills: ',Skills)
print('Volunteer: ', Volunteer)
print('Certificates: ', Certificates)
print('The user has scored:', count, 'points')
