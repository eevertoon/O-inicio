Quest�o 1
class Basics {
	public static void main (String[] args) {
	int x;
	int y;
	int z;
	System.out.println(x+y+z);
	} 
}

Qual o resultado se tentarmos compilar e executar o c�digo acima?
N�o imprime nada Imprime:
Imprime: null
Run time Exception
Erro de compila��o

Questao 2
class Blue {
	public static void main (String[] args) {
	String s = null;
	System.out.print(s);
	}
}

Qual o resultado se tentarmos compilar e executar o c�digo acima?
N�o imprime nada Imprime:
Imprime: null
Run time Exception
Erro de compila��o

Quest�o 3
class Basics1 {
	public void main(String[] args) {}
}
class Basics2 {
	public void main(String []args) {}
}
class Basics3 {
public void main(String args[]) {}
}
Qual o resultado se tentarmos compilar e executar o c�digo acima?
a.Erro de compila��o na linha 2
b.Erro de execu��o na linha 2
c.Erro de execu��o na linha 2 e 5
d.Erro de execu��o na linha 2, 5 e 8

Quest�o 4
class A {
	public static void main (String[] args) {
		// Insira o c�digo aqui.
	}
}

Qual destas linhas pode ser inserida no local especificado acima sem gerar um erro de compila��o?
a.boolean b1 = true;
b.boolean b2 = TRUE;
c.boolean b3 = 'true';
d.boolean b4 = "TRUE";


Quest�o 6
class Violet {
	int x;
	public static void main(String[] args) {
		int y;
		System.out.print("x="+x);
		System.out.print(", y="+y);
	}
}
Qual o resultado se tentarmos compilar e executar o programa acima?
Erro de compila��o na linha 2, 4, 5 e 6.
Erro de compila��o na linha 4, 5 e 6.
Erro de compila��o na linha 5 e 6.
Erro de compila��o na linha 6.


Quest�o 7
Qual � o prop�sito do m�todo main() em um programa Java?

Construir uma interface de usu�rio
Controlar as APIs da aplica��o 
Criar os bot�es e barras de rolagem
Agir como ponto de entrada para o programa

Quest�o 8
Um programa escrito em Java pode rodar em qualquer plataforma porque...
A linguagem Java � derivada do C++
A Maquina Virtual Java (JVM) interpreta o programa para o sistema operacional nativo
O compilador � id�ntico ao compilador do C++
As APIs fazem todo o trabalho


Quest�o 9
Objetivo: Cometer erros e observar como o compilador e sistema de tempo de execu��o respondem aos erros cometidos. Entender o significado das mensagens de erro. O programa a ser tomado como base para o exerc�cio abaixo �:

public class CometendoErros{
	public static void main(String argv[]){
		System.out.println("Hello World");
	}
}

1) Escrever Main ao inv�s de main.
2) Retirar a palavra void da declara��o de main.
3) Trocar o void por int na declara��o de main.
4) Mantendo o tipo de retorno int acrescentar um return 1; ao final do m�todo main.
5) Voltar a colocar o tipo de retorno void, deixando o return 1.
6) Declarar uma vari�vel com o nome dado por uma palavra reservada da linguagem (por exemplo, chamar uma vari�vel de static).

Quest�o 10

Objetivo: Trabalhar com os operadores aritm�ticos, incremento e decremento e de atribui��o compostos.

1) Quais os valores que voc� espera que tenham as vari�veis inteiras z e x ap�s a execu��o da linha seguinte de c�digo?

	z = 1 + (x=5)+2;

Implemente um programa para averiguar se a sua resposta est� correta.

2) Quais os valores que voc� espera que tenham as vari�veis inteiras x, y e z ap�s a execu��o da linha seguinte de c�digo?

	z = 1 + (x=y=5)+2;

Implemente um programa para averiguar se a sua resposta est� correta.

3) Considere as vari�veis inteiras n, m, x e y. Suponha que se tenha atribu�do a m o valor 10, a n o valor 5, a x o valor 1 e a y o valor 3. Qual � o valor que voc� espera que tenham as vari�veis n, m, x e y ap�s as seguintes linhas de c�digo?

a) m += n + x - y;
b) m /= n + x - y;
c) m *= n + x - y;
d) x += y-= m;
e) m = x++ * ++y;
f) m = ++y - x++;
g) m = x++/(y-x);
h) x+= y%2;

Quest�o 11
Escreva um programa java com as seguintes instru��es:

a) Declare que as vari�veis soma e x s�o do tipo inteiro.
b) Atribua 1 a vari�vel x.
c) Atribua 0 a vari�vel soma.
d) Adicione a vari�vel x a vari�vel soma e atribua o resultado a vari�vel soma
e) Imprima �A soma = � seguido pelo valor da vari�vel soma

Quest�o 12 - Escreva um programa que leia via teclado nome, idade, cpf, endere�o e altura do usu�rio. Em seguida imprima na tela os valores lidos.

Quest�o 13 - Escreva um programa que leia via teclado nome, nota 1 e nota 2 de um aluno, calcule a m�dia do aluno e imprima a m�dia na tela.

Quest�o 14 � [Trabalhando com Orienta��o a Objetos]  Siga as orienta��es abaixo e construa um programa em java (OPCIONAL).

1 - Crie uma classe em java chamada  Carro  com os seguintes atributos do tipo String: Modelo, marca, chassi, fabricante. A classe dever� ter os seguintes m�todos: 
ligarCarrro (); //Funcionalidade: Dever� imprimir a mensagem �Carro Ligado�.
desligarCarro(); //Funcionalidade: Dever� imprimir a mensagem �Carro Desligado�.
acelerarCarro(); //Funcionalidade: Dever� imprimir a mensagem �ACELERANDO...�.
frearCarro(); //Funcionalidade: Dever� imprimir a mensagem �FREAANDOO...�.
