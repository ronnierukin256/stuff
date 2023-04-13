import PySimpleGUI as sg
import pandas as pd

# Add some color to the window
sg.theme('DarkTeal9')

EXCEL_FILE = 'mom_bio_data.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
	[sg.Text('BIO DATA')],
	[sg.Text('Please fill out the following fields:')],

	[sg.Text('MOTHER INFORMATION')],
	[sg.Text('Mother_nin', size = (15,1)), sg.InputText(key='Mother_nin')],
	[sg.Text('Mother_surname', size = (15,1)), sg.InputText(key='Mother_surname')],
	[sg.Text('Mother_other_names', size = (15,1)), sg.InputText(key='Mother_other_names')],
	[sg.Text('Alive/Deceased/Unknown', size=(15,1)),
							sg.Checkbox('Alive', key='Alive'),
							sg.Checkbox('Deceased', key='Deceased'),
							sg.Checkbox('Unknown', key='Unknown')],
	[sg.Text('Mother_date_of_birth', size = (15,1)), sg.InputText(key='Mother_date_of_birth')],
	[sg.Text('Mother_card_no.', size = (15,1)), sg.InputText(key='Mother_card_no.')],
	[sg.Text('Mother_date_of_expiry', size = (15,1)), sg.InputText(key='Mother_date_of_expiry')],
	[sg.Text('Mother_district', size = (15,1)), sg.InputText(key='Mother_district')],
	[sg.Text('Mother_county', size = (15,1)), sg.InputText(key='Mother_county')],
	[sg.Text('Mother_sub_county', size = (15,1)), sg.InputText(key='Mother_sub_county')],
	[sg.Text('Mother_parish', size = (15,1)), sg.InputText(key='Mother_parish')],
	[sg.Text('Mother_village', size = (15,1)), sg.InputText(key='Mother_village')],	
	[sg.Text('Mother_occupation', size = (15,1)), sg.InputText(key='Mother_occupation')],
	[sg.Text('Mother_phone_no.', size = (15,1)), sg.InputText(key='Mother_phone_no.')],
	[sg.Text('Mother_oher_phone_no.', size = (15,1)), sg.InputText(key='Mother_oher_phone_no.')],
	[sg.Text('Mother_tribe', size = (15,1)), sg.InputText(key='Mother_tribe')],

	[sg.Submit(), sg.Button("Clear"), sg.Exit()],
]

window = sg.Window('Simple data entry form', layout)

def clear_input():
	for key in values:
		window[key]("")
	return None

while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Exit':
		break
	if event == "Clear":
		clear_input()
	if event == 'Submit':
		df = df.append(values, ignore_index=True)
		df.to_excel(EXCEL_FILE)
		sg.popup('Data saved!')
	else:
		print(event, values)
window.close()
