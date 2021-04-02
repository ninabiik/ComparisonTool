import PySimpleGUI as sg
from comparison import compare_values
from datetime import datetime

menuoptions = [
    [
        sg.Text("Athena's File: ", size=(12, 1)),
        sg.Input(key='FileInput1', size=(30, 1), ),
        sg.FilesBrowse(target='FileInput1', file_types=(("Text Files", "*.xlsx"),))
    ],
[
        sg.Text("Redshift's File", size=(12, 1)),
        sg.Input(key='FileInput2', size=(30, 1), ),
        sg.FilesBrowse(target='FileInput2', file_types=(("Text Files", "*.xlsx"),))
    ],
    [
        sg.Text("Output Folder: ", size=(12, 1)),
        sg.Input(key='OutputFolder', size=(30, 1), ), sg.FolderBrowse(target='OutputFolder')
    ],
    [
        sg.Button("Compare", size=(10, 1), ),
        sg.Button('Cancel', key='Cancel', size=(10, 1), )
    ]

]
layout = [
    [
        sg.Column(menuoptions)
    ]
]

window = sg.Window("Comparison Tool ", layout)
window.Finalize()

while True:
    event, values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    elif event == "Compare":
        #sg.Print('Starting Comparison', do_not_reroute_stdout=False)
        window['Compare'].update(disabled=True)
        current_date = datetime.today()
        print("Start time: {}".format(current_date))
        print("---------------------------------(´・(oo)・｀)---------------------------------")
        inputfile1 = values['FileInput1']
        inputfile2 = values['FileInput2']
        outfolder = values['OutputFolder']
        comparison = compare_values(inputfile1)
        comparison.set_output_path(outfolder)
        comparison.compare_values()
        # kpidata = compare.getKPI()
        # countList = [x['ERROR_COUNT'] for x in kpidata]
        # kpiLabels = [x['KPI'] for x in kpidata]
        # draw_plot(kpiLabels, countList, firstenv, secondenv)
        finished_time = datetime.today()
        print("---------------------------------(´・(oo)・｀)---------------------------------")
        print("End Time: {}".format(finished_time))
        elapsedtime = finished_time - current_date
        print("Elapsed Time: {}".format(elapsedtime))
        # sg.SystemTray.notify('Comparison Completed', 'Comparison for {} and {} is completed.\nElapsed Time: {}.  Please check the result in the output folder that you specified'.format(firstenv, secondenv, elapsedtime))
        sg.popup('Comparison Completed',
                 'Data Comparison completed between Athena and Redshift Data. Please check the results in the specifed output folder.\n\nElapsed time: {} '.format(
                     finished_time - current_date))
        window['Compare'].update(disabled=False)
        window['combo1'].update("Dev")
        window['combo2'].update("Prod")
        window['FileInput'].update("")
        window['OutputFolder'].update("")

window.close()