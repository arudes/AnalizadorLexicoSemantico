txt = " "
cont =0
def incrementarContador():
	global cont
	cont +=1
	return "%d" %cont
class Nodo():
	pass

def p_program(Nodo):
	def __init__(self,son1,name):
		self.name=name
		self.son1=son1

	def imprimir(ident):
		self.son1.imprimir(" "+ident)
		print(ident +"Nodo: "+self.name)

	def traducir(self):
		global txt
		id=incrementarContador()
		son1=self.son1.traducir()
		txt+=id+"[label="+self.name+"]"+"\n\t"
		txt+=id+"->"son1+"\n\t"
		return "digraph G {\n\t"+txt+"}"


def p_block(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def  p_constDecl(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_constDeclEmpty(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_constAssigmentList(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_constAssigmentList2(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_varDecl1(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_varDeclEmpty(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_identList1(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_identList2(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_procDecl1(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_procDeclEmpty(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_statement1(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_statement2(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_statement3(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_statement4(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_statement5(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_statementEmpty(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_statementList1(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_statementList2(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_condicion1(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_condicion2(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_relation1(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_relation2(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_relation3(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_relation4(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_relation5(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_relation6(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_expression1(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_expression2(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_expression3(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_expression5(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_term1(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_term2(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_multiplyingOperator1(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_multiplyingOperator2(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_factor1(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_factor(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_factor3(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_empty(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id


def p_error(Nodo):
	def __init__(self,name):
		self.name=name

	def imprimir(ident):
		self.

	def traducir(self):
		global txt
		id=incrementarContador()
		return id