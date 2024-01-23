import PySimpleGUI as sg

def homeInfermiere(infermiere):
    sg.theme('DarkAmber')

    layout = [
        [sg.Text(f'Benvenuto {infermiere.nome} {infermiere.cognome}')],
        [sg.Text('Inserire il codice fiscale del paziente:'), sg.InputText(), sg.Button('Ok')],
        [ sg.Button('Indietro'), sg.Button('Profilo')]
    ]

    windowHome = sg.Window('Home', layout)

    while True:
        event, codiceFiscale = windowHome.read()

        if event == sg.WINDOW_CLOSED or event == 'Indietro':
            break
        elif event == 'Ok':
            paziente = ricercaPaziente(codiceFiscale)
            cartella = ricercaCartella(codiceFiscale)
            if cartella:
                windowHome.Hide()
                cartellaPaziente(paziente, cartella, windowHome)
            break

    windowHome.close()

def cartellaPaziente(paziente, cartella, windowHome):
    sg.theme('DarkAmber')

    layout = [
        [sg.Text(f'Cartella di {paziente.nome} {paziente.cognome}')],
        [sg.Text(f'Dati Paziente:')],
        [sg.Text(f'Nome: {paziente.nome}')],
        [sg.Text(f'Cognome: {paziente.cognome}')],
        [sg.Text(f'Età: {paziente.età}')],
        [sg.Text('Note:')],
        [sg.Listbox(values=paziente.note, size=(30, 5)), sg.Button('Aggiungi nota')], #vettore non funzionerà mai così
        [sg.Button('Chiudi'), sg.Button('Conferma')]
    ]

    windowCartella = sg.Window('Cartella Paziente', layout)

    while True:
        event, values = windowCartella.read()

        if event == sg.WINDOW_CLOSED or event == 'Chiudi':
            break
        elif event == 'Aggiungi':
            nota_inserita = values['nota_input']
            if nota_inserita:
                aggiungiNotaPaziente(paziente,cartella)

    windowCartella.close()
    windowHome.UnHide()

def aggiungiNotaPaziente(paziente,cartella):
    sg.theme('DarkAmber')

    layout = [
        [sg.Text(f'Aggiungi Nota per {paziente.nome} {paziente.cognome}')],
        [sg.Text('Nuova Nota:'), sg.InputText(key='nuova_nota')],
        [sg.Button('Aggiungi'), sg.Button('Annulla')]
    ]

    windowAggiungiNota = sg.Window('Aggiungi Nota', layout)

    while True:
        event, values = windowAggiungiNota.read()

        if event == sg.WINDOW_CLOSED or event == 'Annulla':
            break
        elif event == 'Aggiungi':
            nuova_nota = values['nuova_nota']
            if nuova_nota:
                conferma = sg.popup_ok_cancel(f'Confermi di voler aggiungere la nota?')
                if conferma == 'OK':
                    cartella.note.append(nuova_nota)
                    sg.popup(f'Nota aggiunta.')
                    break

    windowAggiungiNota.close()

def ricercaPaziente(codiceFiscale):
    pass

def ricercaCartella(codiceFiscale):
    pass

