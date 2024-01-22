import Classi.Medico
import PySimpleGUI as sg
from Classi import Medico
from Classi import Fascicolo
from ProfiloMedico import profiloMedico
from FascicoloPaziente import fascicoloPaziente

def homeMedico(medico):
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Inserire il codice fiscale di un paziente per vedere il suo fascicolo'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Profilo')] ]

    # Create the Window
    window = sg.Window('Home', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, codiceFiscale = window.read() #SANIFICARE
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Profilo':
            profiloMedico(medico)
            break
        if event == 'Ok':
            ricercaPaziente(codiceFiscale)

    window.close()


homeMedico('asd')
def ricercaPaziente(codiceFiscale):
    pass