import datetime

#modulo 'import strftime'
data_hora_atual = datetime.datetime.now()
data_formatada = data_hora_atual.strftime('%D/%m/%Y %h:%m:%S')
