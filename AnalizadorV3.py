import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = ['BEGIN','END','IF','THEN','WHILE','DO','CALL',
'CONST','INT','PROCEDURE','OUT','IN','OR',
'NOT','MENORQUE','MAYORIGUAL','MAYORQUE','MENORIGUAL',
'DISTINTO','NUMERAL','PARIZQ','PARDER','CORIZQ','CORDER',
'LLAIZQ','LLADER','PUNTOCOMA','COMADOBLE',
'VAR','LT','GT','LTE','GTE']

tokens = reservadas+['ID','NUMERO','PLUS','MINUS','DIV','ASIGNAR',
'DOT','UPDATE','COMA','INCLUDE','CADENA','MULT','NAMESPACE',
'VOID','COUT','RETURN','POTENCIA','PUNTO']

"""reservadas = {'begin':'BEGIN',
				'end':'END',
				'if':'IF',
				'then':'THEN',
				'while':'WHILE',
				'do':'DO',
				'call':'CALL',
				'const':'CONST',
				'int':'INT',
				'procedure':'PROCEDURE',
				'out':'OUT',
				'in':'IN',
				'else':'ELSE',
				'and':'AND',
				'or':'OR',
				'not':'NOT',
				'menorque':'MENORQUE',
				'menorigual':'MANORIGUAL',
				'mayorque':'MAYORQUE',
				'mayorigual':'MAYORIGUAL',
				'distinto':'DISTINTO',
				'numeral':'NUMERAL',
				'parizq':'PARIZQ',
				'parder':'PARDER',
				'corizq':'CORIZQ',
				'corder':'CORDER',
				'llaizq':'LLAIZQ',
				'llader':'LLADER',
				'puntocoma':'PUNTOCOMA',
				'comadoble':'COMADOBLE',
				'mayorder':'MAYORDER',
				'modulo':'MODULO',
				'mayorizq':'MAYORIZQ'} 

tokens = tokens + list(reservadas.values())"""

t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'/'
#t_MODULO = r'\%' 
t_POTENCIA = r'(\*{2} | \^)' 
t_ASIGNAR = r'='
#t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PUNTOCOMA = ';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_COMADOBLE = r'\"'
t_PUNTO = r'\.'
t_UPDATE = r':='

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		t.type = t.value 
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMENTARIO(t):
	r'\#.*'
	pass

def t_NUMERO(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	print("Caracter ilegal '%s'" %t.value[0])
	t.lexer.skip(1)

'''def buscarFicheros(directorio):
        ficheros=[]
        numArchivo=''
        respuesta = False
        cont = 1
        for base, dirs, files in os.walk(directorio):
                ficheros.append(files)
        for file in files:
                print(str(cont) +". "+file)
                cont = cont+1
        while respuesta == False:
                numArchivo = input("\nNumero del test: ")
                for file in files:
                        if file == files[int(numArchivo)-1]:
                                respuesta =True
                                break
        print("Has escogido \"%s\" \n" %files[int(numArchivo)-1])
        return files[int(numArchivo)-1]	


directorio = '/Users/AruMou/Documents/Inteligencia Artificial/Compilador 2018/test/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close() '''

analizador = lex.lex()
#analizador.input(cadena)
'''while True:
	tok = analizador.token()
	if not tok :
		break
	print(tok)
'''