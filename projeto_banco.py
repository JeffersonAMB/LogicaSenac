#tela inicial do banco
import modulo_banco
saldo = 0
opcoes = 's'
emprestimo = 500
respostas = 'sim'


cpf_cliente = input('digite seu cpf:')
modulo_banco.verif_dicionario(cpf_cliente)