import PySimpleGUI as sg
import pymysql
from tela import login , cadastro
from senhar_segreda import senhar_segreda


host = pymysql.connect(host='localhost', user='root', password='',db='paz')


loginl, cadastrol = login(), None # QUADANHADO VALIRAVO 
while True: 
    window, event, values = sg.read_all_windows()  # QUADANHADO VALIRAVO
    usuario = values['usuario']
    senhar=values['senhar']
    # email= values['email']
    senhar2=senhar_segreda(senhar) # modifigafosenhar

    if window == loginl and event == sg.WIN_CLOSED:break

    if window == cadastrol and event == sg.WIN_CLOSED:break 
    
    if window == loginl and event == 'Cria':
        cadastrol = cadastro()
        loginl.hide()

    if window == cadastrol and event == 'Cadastra':
        if usuario == ""  and senhar =='':
            sg.popup('campos esta vazio')
        else:
            if window == cadastrol and values['senhar'] == values['c_senhar']:
                if len(senhar)<8: 
                    sg.popup('erro campo senha e menos que 8')
                elif usuario == '':
                    sg.popup('erro campo login esta vazio')
    
                else:
                    try:
                        curso=host.cursor()
                        sql = "INSERT INTO cadastro (usuario,senhar) VALUES(%s,%s)"
                        valor= (usuario,senhar2,)
                        curso.execute(sql, valor)
                        host.commit()
                        cadastrol.hide()
                        loginl.un_hide()
                    except pymysql.err.Error as erro:
                        sg.popup(erro)
            
            else:
                sg.popup('as senharas não esta iguais ')


    if window == loginl and event == "Entra":

        try:
            curso=host.cursor()
            sql = "select id, usuario from cadastro where usuario = %s and senhar = %s"
            valor= (usuario,senhar2,)
            curso.execute(sql, valor)
            senhar_b = curso.fetchall()
           
            if senhar2 == senhar_b[0]:
                host.commit()
            sg.popup('1')
        except:
            sg.popup("nao achei ")

            
    if window == cadastrol and event =='Voltar':
        cadastrol.hide()
        loginl.un_hide()
         
