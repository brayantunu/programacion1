
import java.util.Scanner;

/*

 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author ASUS
 */
public class algoritmia {

    public static void main(String[] args) {
       // brayan2();
        //brayan4();
        //brayan5();
        //brayan6();
        //brayan7();
        //brayan9();
         //brayan12();
        //brayan13();
        //brayan14();
        brayan15();
    }

    public static void brayan2() {
        Scanner teclado = new Scanner(System.in);

        int num1 = 0;
        int num2 = 0;
        int num3 = 0;
        int recibe = 0;

        System.out.println("ingrese los numeros para dividir");
        num1 = teclado.nextInt();
        num2 = teclado.nextInt();
        if (num1 < num2) {
            System.out.println("error en el numero divisor ingrese otro numero que se pueda dividir");
            num1 = teclado.nextInt();
            num2 = teclado.nextInt();
        }
        while (num2 != 0) {
            recibe = num2;
            num2 = num1 % num2;
            num1 = recibe;
        }
        System.out.println(num1);

    }

    public static void brayan3() {
        int num1 = 0;
        int serie = 0;

    }

    public static void brayan4() {
        int num1 = 2;
        int serie = 0;
        for (num1 = 2; num1 <= 99; num1 = num1 + 2) {
            System.out.println(num1);
        }
    }

    public static void brayan5() {
        Scanner teclado = new Scanner(System.in);
        int num1 = 0;
        int num2 = 0;
        int num3 = 0;
        int num4 = 0;

        System.out.println("ingrese 4 numeros para sabe cual es el mayor");
        num1 = teclado.nextInt();
        num2 = teclado.nextInt();
        num3 = teclado.nextInt();
        num4 = teclado.nextInt();

        if (num1 != num2 && num1 != num3 && num1 != num4 && num2 != num3 && num1 != num4 && num3 != num4) {
            if (num1 > num2) {
                if (num1 > num3) {
                    if (num1 > num4) {
                        System.out.println("el mayor es " + num1);
                    } else {
                        System.out.println("el mayor es " + num4);
                    }

                } else {
                    if (num3 > num4) {
                        System.out.println("el mayor es " + num3);
                    } else {
                        System.out.println("el mayor es" + num4);
                    }
                }
            } else {
                if (num2 > num3) {
                    if (num2 > num4) {
                        System.out.println("el mayor es " + num2);
                    } else {
                        System.out.println("el mayor es " + num4);
                    }
                } else {
                    if (num3 > num4) {
                        System.out.println("el mayor es " + num3);
                    } else {
                        System.out.println("el mayor es " + num4);
                    }
                }
            }

        } else {
            System.out.println("los numeros no son diferentes");
        }

    }

    public static void brayan6() {
        Scanner teclado = new Scanner(System.in);
        int numero1 = 0;
        boolean recibe;

        System.out.println("ingrese un numero para saber si es primo");
        numero1 = teclado.nextInt();

       recibe = numero1 % 2 == 0;
        
        
    }
    

    public static void brayan7(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese Cantidad de Numeros a Analizar");
        int n = sc.nextInt();
        int sumaImpar = 0;
        int sumaPar = 0;
        for (int i = 1; i <= n; i++) {
            System.out.println(" Ingrese numero " + i
            );
            int num = sc.nextInt();
            if (num % 2 == 0) {
                sumaPar = sumaPar + num;
            } else {
                sumaImpar = sumaImpar + num;
            }
        }
        System.out.println(" Suma de numeros Par " + sumaPar);
        System.out.println(" Suma de numeros Impares " + sumaImpar);
    }

    public static void brayan9() {
        Scanner teclado = new Scanner(System.in);
        int suma = 0;
        double producto = 1;
        int contador = 20;

        do {

            producto = producto * contador;
            suma = suma + contador;
            contador = contador + 2;
            System.out.println(contador);

        } while (contador < 100);
        System.out.println("el resultado del producto " + producto);
        System.out.println("el resultado de la suma es " + suma);

    }

    public static void brayan12() {
        int i = 0;
        int suma = 0;

        for (i = 1; i < 100; i++) {
            suma = suma + (i * i);

        }
        System.out.println("la suma de los cuadrados del 1 es" + suma);

    }

    public static void brayan13() {
        Scanner teclado = new Scanner(System.in);
        int num1 = 0, num2 = 0;
        int i = 0;

        System.out.println("ingrese un numero multiplos");
        num1 = teclado.nextInt();
        System.out.println("ingrese el numero hasta terminar");
        num2 = teclado.nextInt();

        System.out.println("los multiplos de " + num1);
        for (i = num1; i >= num2; i += -4) {
            System.out.println("- " + i);
        }

    }

    public static void brayan14() {
        Scanner teclado = new Scanner(System.in);

        int n1 = 0;
        int n2 = 0;
        int n3 = 0;

        System.out.println("ingrese 3 numero para calcular cual es el central");
        n1 = teclado.nextInt();
        n2 = teclado.nextInt();
        n3 = teclado.nextInt();

        if (n1 != n2 && n1 != n3 && n2 != n3) {
            if (n1 > n2) {
                if (n1 > n3) {
                    System.out.println("el numero central es " + n1);
                } else {
                    System.out.println("el numero central es " + n3);
                }

            } else {
                if (n2 > n3) {
                    System.out.println("el numero central es " + n2);
                } else {
                    System.out.println("el numero central es " + n3);

                }

            }

        } else {
            System.out.println("los numeros se repiten vuelva a intentar otra vez");
        }
    }

    public static void brayan15() {
        Scanner teclado = new Scanner(System.in);
        int n1 = 0;
        int n2 = 0;
        int raiz = 0;
        System.out.println("ingrese el numero para calcular la raiz");
        n1 = teclado.nextInt();

        raiz = n1 * n2;
       
            

        System.out.println("la raiz cuadrada es " + raiz);

    }
}
