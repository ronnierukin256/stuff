import PySimpleGUI as sg
import pandas as pd

# Add some color to the window
sg.theme('DarkTeal9')

EXCEL_FILE = 'applicant_nid_bio_data.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
	[sg.Text('BIO DATA')],
	[sg.Text('Please fill out the following fields:')],
	
	[sg.Text('FULL NAMES')],
	[sg.Text('Surname', size = (15,1)), sg.InputText(key='Surname')],
	[sg.Text('Other_names', size = (15,1)), sg.InputText(key='Other_names')],
	
	[sg.Text('IDENTIFICATION INFORMATION' )],
	[sg.Text('NATIONAL ID INFORMATION')],
	[sg.Text('Nin', size = (15,1)), sg.InputText(key='Nin')],
	[sg.Text('Date_of_birth', size = (15,1)), sg.InputText(key='Date_of_birth')],
	[sg.Text('Card_no.', size = (15,1)), sg.InputText(key='Card_no.')],
	[sg.Text('Date_of_expiry', size = (15,1)), sg.InputText(key='Date_of_expiry')],
	[sg.Text('District', size = (15,1)), sg.InputText(key='District')],
	[sg.Text('County', size = (15,1)), sg.InputText(key='County')],
	[sg.Text('Sub_county', size = (15,1)), sg.InputText(key='Sub_county')],
	[sg.Text('Parish', size = (15,1)), sg.InputText(key='Parish')],
	[sg.Text('Village', size = (15,1)), sg.InputText(key='Village')],

	[sg.Submit(), sg.Button("Clear"), sg.Exit()],
]

window = sg.Window('Simple data entry form', layout)

def clear_input():
	for key in values:
		window[key]("")
	return None


while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == "Exit":
		break
	if event == "Clear":
		clear_input()
	if event == 'Submit':
		df = df.append(values, ignore_index=True)
		df.to_excel(EXCEL_FILE)
		sg.popup('Data saved!')
		clear_input()
	else:
		print(event, values)
window.close()
