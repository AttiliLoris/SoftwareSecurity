import PySimpleGUI as sg
from Classi import Medico
from Classi import Fascicolo

def homeMedico(medico):
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layoutHome = [[sg.Text('Inserire il codice fiscale di un paziente per vedere il suo fascicolo'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Profilo')] ]

    # Create the Window
    windowHome = sg.Window('Home', layoutHome)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, codiceFiscale = windowHome.read() #SANIFICARE
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Profilo':
            windowHome.Hide()
            profiloMedico(medico, windowHome)
        if event == 'Ok':
            ricercaPaziente(codiceFiscale)

    windowHome.close()

def profiloMedico(medico, windowHome):
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layoutProfilo = [[sg.Text('Nome'), sg.InputText(medico.nome)],
              [sg.Text('Cognome'), sg.InputText(medico.cognome)],
              [sg.Text('Codice fiscale'), sg.InputText(medico.codiceFiscale)],
              [sg.Button('Salva'), sg.Button('Home')]]

    # Create the Window
    windowProfilo = sg.Window('Home', layoutProfilo)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, valoriInput = windowProfilo.read()  # SANIFICARE
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == 'Home':
            break
        if event == 'Salva':
            if controllaValori(valoriInput):
                pass
            else:
                break
    windowProfilo.close()
    windowHome.UnHide()

def controllaValori(valoriInput):
    for elemento in valoriInput:
        if valoriInput[elemento] == '':
            sg.popup_error('Uno dei campi è vuoto, inserire un input valido')
            return 1
    medico.salva(valoriInput)

medico = Medico.Medico('Loris', 'Attili', 'CF1')
homeMedico(medico)


def ricercaPaziente(codiceFiscale):
    pass