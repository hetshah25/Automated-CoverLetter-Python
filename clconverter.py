from docxtpl import DocxTemplate
import datetime

company_name = input("Enter name of the Company : ")
position_name = input("Enter name of the Position: ")
add_fline = input("Enter the first line of address: ")
add_sline = input("Enter the second line of address: ")

# Today's date with date format
today_date = datetime.datetime.today().strftime('%B %d, %Y')

context = {
    'today_date': today_date,
    'company_name': company_name,
    'position_name': position_name,
    'add_fline': add_fline,
    'add_sline': add_sline
}

# Opening our template
doc = DocxTemplate("Cover_Letter.docx")

# Load this doc
doc.render(context)
doc.save('Cover_letter_'+company_name+'_'+position_name+'.docx')
