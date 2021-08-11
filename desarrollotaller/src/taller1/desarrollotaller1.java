package taller1;
import java.util.Scanner;
public class desarrollotaller1 {
    public static void main(String[] args) {
        Conjuntos met = new Conjuntos();
        met.menu();
    }
}
class Conjuntos {
    int[] A, B, C;
    int tamañoA, tamañoB, x = 0;
    Scanner entrada = new Scanner(System.in);

    public void llenarA() {
        System.out.println( "Ingrese el tamaño del grupo A\n");
         tamañoA = entrada.nextInt();
        A = new int[tamañoA];

        for (int i = 0; i < tamañoA; i++) {
            System.out.println("Ingrese un nùmero para A= ");
            A[i] = entrada.nextInt();
        }
    }

    public void llenarB() {
    	System.out.println( "Ingrese el tamaño del grupo B\n");
        tamañoB = entrada.nextInt();
        B = new int[tamañoB];

        for (int i = 0; i < tamañoB; i++) {
            System.out.println("Ingrese un nùmero para B= ");
            B[i] = entrada.nextInt();
        }
    }

    public void Union() {
        C = new int[100];

        for (int x = 0; x < A.length; x++) {
            for (int y = 0; y < B.length; y++) {
                if (A[x] == B[y]) {
                    A[x] = 0;
                }
            }
        }

        System.out.println( "La Union del grupo A y B es =\n");
        for (int x = 0; x < A.length; x++) {
            if (A[x] != 0) {
                System.out.println(A[x]);
            }
        }

        for (int x = 0; x < B.length; x++) {
            System.out.println(B[x]);
        }
    }

    public void Interseccion() {
        int z = 0;
        C = new int[100];

        for (int x = 0; x < A.length; x++) {
            for (int y = 0; y < B.length; y++) {
                if (A[x] == B[y]) {
                    C[z] = A[x];
                    z++;
                }
            }
        }

        System.out.println( "La intersección del grupo A con el B es = \n");
        for (int x = 0; x < z; x++) {
            System.out.print(C[x] + " - ");
        }
    }

    public void Diferencia() {
        C = new int[100];
        int k = 0, cont;

        for (int x = 0; x < A.length; x++) {
            cont = 0;
            for (int y = 0; y < B.length; y++) {
                if (A[x] == B[y]) {
                    cont++;
                }
            }

            if (cont == 0) {
                C[k] = A[x];
                k++;
            }

        }

        System.out.println( "La diferencia de A - B es =\n");
        for (int x = 0; x < k; x++) {
            System.out.print(C[x] + " - ");
        }
    }
    public void menu() {
        int opc;
        System.out.println("\n\ntaller#1-CONJUNTOS\n"
                +"1.Uniòn\n"
                + "2.Intersecciòn\n"
                + "3.A diferencia B\n"
                + "4.Salir\n");
        System.out.println("Seleccione la operación que quiere llevar a cabo: \n");

        opc = entrada.nextInt();
        switch (opc) {
            case 1:
                llenarA();
                llenarB();
                Union();
                menu();
                break;
            case 2:
                llenarA();
                llenarB();
                Interseccion();
                menu();
                break;
            case 3:
                llenarA();
                llenarB();
                Diferencia();
                menu();
                break;
            case 4:
                System.out.println("Gracias por utilizar nuestro programa, vuelve pronto\n"
);
                break;
            default:
                menu();
                break;
        }
    }
}
