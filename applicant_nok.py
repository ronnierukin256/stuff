import PySimpleGUI as sg
import pandas as pd

# Add some color to the window
sg.theme('DarkTeal9')

EXCEL_FILE = 'nok_bio_data.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
	[sg.Text('BIO DATA')],
	[sg.Text('Please fill out the following fields:')],

	[sg.Text('KIN INFORMATION')],
	[sg.Text('NEXT OF KIN INFORMATION (Nok)')],
	[sg.Text('Nok_nin', size = (15,1)), sg.InputText(key='Nok_nin')],
	[sg.Text('Nok_surname', size = (15,1)), sg.InputText(key='Nok_surname')],
	[sg.Text('Nok_other_names', size = (15,1)), sg.InputText(key='Nok_other_names')],
	[sg.Text('Alive/Deceased/Unknown', size=(15,1)),
							sg.Checkbox('Alive', key='Alive'),
							sg.Checkbox('Deceased', key='Deceased'),
							sg.Checkbox('Unknown', key='Unknown')],
	[sg.Text('Nok_relationship', size = (15,1)), sg.Combo(['Father', 'Mother', 'Brother', 'Sister','Uncle', 'Aunt'], key='Nok_relationship')],
	[sg.Text('Nok_gender', size=(15,1)), sg.Combo(['Male', 'Female',], key='Nok_gender')],
	[sg.Text('Nok_date_of_birth', size = (15,1)), sg.InputText(key='Nok_date_of_birth')],
	[sg.Text('Nok_date_of_expiry', size = (15,1)), sg.InputText(key='Nok_date_of_expiry')],
	[sg.Text('Nok_district', size = (15,1)), sg.InputText(key='Nok_district')],
	[sg.Text('Nok_county', size = (15,1)), sg.InputText(key='Nok_county')],
	[sg.Text('Nok_sub_county', size = (15,1)), sg.InputText(key='Nok_sub_county')],
	[sg.Text('Nok_parish', size = (15,1)), sg.InputText(key='Nok_parish')],
	[sg.Text('Nok_village', size = (15,1)), sg.InputText(key='Nok_village')],
	[sg.Text('Nok_occupation', size = (15,1)), sg.InputText(key='Nok_occupation')],	
	[sg.Text('Nok_phone_no.', size = (15,1)), sg.InputText(key='Nok_phone_no.')],
	[sg.Text('Nok_other_phone_no.', size = (15,1)), sg.InputText(key='Nok_other_phone_no.')],

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
