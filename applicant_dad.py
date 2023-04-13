import PySimpleGUI as sg
import pandas as pd

# Add some color to the window
sg.theme('DarkTeal9')

EXCEL_FILE = 'dad_bio_data.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
	[sg.Text('BIO DATA')],
	[sg.Text('Please fill out the following fields:')],


	[sg.Text('FATHER INFORMATION')],
	[sg.Text('Father_nin', size = (15,1)), sg.InputText(key='Father_nin')],
	[sg.Text('Father_surname', size = (15,1)), sg.InputText(key='Father_surname')],
	[sg.Text('Father_other_names', size = (15,1)), sg.InputText(key='Father_other_names')],
	[sg.Text('Alive/Deceased/Unknown', size=(15,1)),
							sg.Checkbox('Alive', key='Alive'),
							sg.Checkbox('Deceased', key='Deceased'),
							sg.Checkbox('Unknown', key='Unknown')],
	[sg.Text('Father_date_of_birth', size = (15,1)), sg.InputText(key='Father_date_of_birth')],
	[sg.Text('Father_card_no.', size = (15,1)), sg.InputText(key='Father_card_no.')],
	[sg.Text('Father_date_of_expiry', size = (15,1)), sg.InputText(key='Father_date_of_expiry')],
	[sg.Text('Father_district', size = (15,1)), sg.InputText(key='Father_district')],
	[sg.Text('Father_county', size = (15,1)), sg.InputText(key='Father_county')],
	[sg.Text('Father_sub_county', size = (15,1)), sg.InputText(key='Father_sub_county')],
	[sg.Text('Father_parish', size = (15,1)), sg.InputText(key='Father_parish')],
	[sg.Text('Father_village', size = (15,1)), sg.InputText(key='Father_village')],	
	[sg.Text('Father_occupation', size = (15,1)), sg.InputText(key='Father_occupation')],
	[sg.Text('Father_phone_no.', size = (15,1)), sg.InputText(key='Father_phone_no.')],
	[sg.Text('Father_oher_phone_no.', size = (15,1)), sg.InputText(key='Father_oher_phone_no.')],
	[sg.Text('Father_clan', size = (15,1)), sg.InputText(key='Father_clan')],
	[sg.Text('Father_tribe', size = (15,1)), sg.InputText(key='Father_tribe')],
	[sg.Text('Father_descendant_name_one', size = (15,1)), sg.InputText(key='Father_descendant_name_one')],
	[sg.Text('Father_descendant_name_two', size = (15,1)), sg.InputText(key='Father_descendant_name_two')],



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
