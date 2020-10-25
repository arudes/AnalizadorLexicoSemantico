import ply.yacc as yacc
import os
import codecs
import re
from AnalizadorV3 import tokens
from sys import stdin

precedence = (
    ('right','ID','CALL','BEGIN','IF','WHILE')
    ('right','PROCEDURE')
    ('right','VAR')
    ('right','ASIGNAR'),
    ('right','UPDATE'),
    ('left','DISTINTO'),
    ('left','LT','LTE','GT','GTE')
    ('left','PLUS','MINUS'),
    ('left','MULT','DIV'),
    ('left','PARIZQ','PARDER'),
)

def p_program(p):
    ''' program : block '''
    # print("program")
    p[0] = program(p[1],"program")

def p_block(p):
    '''block : constDecl varDecl procDecl statement'''
    # print("block")
    p[0]=block(p[1],p[2],p[3],p[4],"block")

def  p_constDecl(p):
    '''constDecl : CONST constAssigmentList PUNTOCOMA'''
    p[0] = constDecl(p[2],"constDecl")
    # print("constDecl")

def p_constDeclEmpty(p):
    '''constDecl : empty'''
    p[0] = Null()
    # print("nulo")

def p_constAssigmentList1(p):
    '''constAssigmentList : ID ASSIGN NUMBER'''
    # print("constAssigmentList 1")
    p[0]= constAssigmentList1(Id(p[1]),Assign(p[2]),Number(p[3]),"constAssigmentList1")

def p_constAssigmentList2(p):
    '''constAssigmentList : constAssigmentList COMA ID ASSIGN NUMBER'''
    # print("constAssigmentList 2")

def p_varDecl1(p):
    '''varDecl : VAR identList COMA ID'''
    print("varDecl 1")

def p_varDeclEmpty(p):
    '''varDecl : empty'''
    print("nulo")

def p_identList1(p):
    '''identList : ID'''
    print("identList 1")

def p_identList2(p):
    '''identList : identList COMMA ID'''
    print("identList 2")

def p_procDecl1(p):
    '''procDecl : procDecl PROCEDURE ID PUNTOCOMA block PUNTOCOMA'''
    print("procDecl 1")

def p_procDeclEmpty(p):
    '''procDecl : empty'''
    print("nulo")

def p_statement1(p):
    '''statement : ID UPDATE expression'''
    print("statement 1")

def p_statement2(p):
    '''statement : CALL ID'''
    print("statement 2")

def p_statement3(p):
    '''statement : BEGIN statementList END'''
    print("statement 3")

def p_statement4(p):
    '''statement : IF condition THEN statement'''
    print("statement 4")

def p_statement5(p):
    '''statement : WHILE condition DO statement'''
    print("statement 5")

def p_statementEmpty(p):
    '''statement : empty'''
    print("nulo")

def p_statementList1(p):
    '''statementList : statement'''
    print("statementList 1")

def p_statementList2(p):
    '''statementList : statementList PUNTOCOMA statement'''
    print("statementList 2")

def p_condicion1(p):
    '''condition : DISTINTO expression'''
    print("condicion 1")

def p_condicion2(p):
    '''condition : expression relation expression'''
    print("condicion 2")

def p_relation1(p):
    '''relation : ASSIGN'''
    print("relacion 1")

def p_relation2(p):
    '''relation : DISTINTO'''
    print("relacion 2")

def p_relation3(p):
    '''relation : LT'''
    print("relacion 3")

def p_relation4(p):
    '''relation : GT'''
    print("relacion 4")

def p_relation5(p):
    '''relation : LTE'''
    print("relacion 5")

def p_relation6(p):
    '''relation : GTE'''
    print("relacion 6")

def p_expression1(p):
    '''expression : term'''
    print("expresion 1")

def p_expression2(p):
    '''expression : addingOperator term'''
    print("expresion 2")

def p_expression3(p):
    '''expression : expresion addingOperator term'''
    print("expresion 3")

def p_expression4(p):
    '''addingOperator : PLUS'''
    print("expresion 4")

def p_expression5(p):
    '''addingOperator : MINUS'''
    print("expresion 5")

def p_term1(p):
    '''term : factor'''
    print("term 1")

def p_term2(p):
    '''term : term multiplyingOperator factor'''
    print("term 2")

def p_multiplyingOperator1(p):
    '''multiplyingOperator : MULT'''
    print("multiplyingOperator 1")

def p_multiplyingOperator2(p):
    '''multiplyingOperator : DIV'''
    print("multiplyingOperator 2")

def p_factor1(p):
    '''factor : ID'''
    print("factor 1")

def p_factor(p):
    '''factor : NUMBER'''
    print("factor 2")

def p_factor3(p):
    '''factor : PARIZQ expression PARDER'''
    print("factor 3")

def p_empty(p):
    '''empty : empty'''
    pass

def p_error(p):
    print("Error de sintaxis",p)
    print("Error en la linea" +str(p.lineno))

def buscarFicheros(directorio):
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

directorio = '/Users/Maldonado/Documents/Inteligencia artificial/Compilador 2018/test/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
resultado = parser.parse(cadena)

# resultado.imprimir(" ")
# print(result.traducir())

# graphFile = open('graphviztrhee.vz','w')
# graphFile.write(resultado.traducir())
# graphFile.close()
print(resultado)
