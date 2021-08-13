package desarrollotaller2;

import static java.awt.PageAttributes.MediaType.D;
import java.util.HashSet;

public class Desarrollotaller2 {

    public static void main(String[] args) {
        HashSet<Integer> A = new HashSet<>();
        for (int i = 3; i <= 20; i++) {
            A.add(i);
        }

        //Conjunto B
        HashSet<Integer> B = new HashSet<>();
        for (int i = 1; i <= 27; i++) {
            if (i % 2 == 0) {
                B.add(i);
            }
        }
        //Conjunto C
        HashSet<Integer> C = new HashSet<>();
        C.add(1);
        C.add(4);
        C.add(7);
        C.add(8);
        C.add(10);
        C.add(14);
        C.add(17);
        C.add(20);

        //Conjunto  D
        HashSet<Integer> D = new HashSet<>();
        D.add(2);
        D.add(3);
        D.add(5);
        D.add(7);
        D.add(11);
        D.add(13);
        D.add(17);
        D.add(19);
        D.add(23);
        D.add(29);
        D.add(31);
        D.add(37);
        D.add(41);
        D.add(43);
//Operación 1
        HashSet<Integer> O1 = diferenciasimetrica(interseccion(A, C), B);
        System.out.println("Operación 1: " + O1);
       
        
//Operación 2
HashSet<Integer> O2 = diferencia(union(C, A), D);
        System.out.println("Operación 2: " + O2);
        
//Operación 3
HashSet<Integer> O3 = union(A,diferenciasimetrica(B, C));
        System.out.println("Operación 3: " + O3);

//Operación 4
HashSet<Integer> O4 = diferencia(interseccion(A, D),diferenciasimetrica(B,C));
        System.out.println("Operación 4: " + O4);

    }
  

  

    // Función unión
    public static HashSet<Integer> union(HashSet<Integer> c1, HashSet<Integer> c2) {
        HashSet<Integer> resultado = new HashSet<>();
        resultado.addAll(c1);
        resultado.addAll(c2);
        return resultado;
    }

    //Función intersección
    public static HashSet<Integer> interseccion(HashSet<Integer> c1, HashSet<Integer> c2) {
        HashSet<Integer> resultado = new HashSet<>();
        resultado.addAll(c1);
        resultado.retainAll(c2);
        return resultado;
    }

    // Función diferencia
    public static HashSet<Integer> diferencia(HashSet<Integer> c1, HashSet<Integer> c2) {
        HashSet<Integer> resultado = new HashSet<>();
        resultado.addAll(c1);
        resultado.removeAll(c2);
        return resultado;
    }

//Función diferencia simetrica 
    public static HashSet<Integer> diferenciasimetrica(HashSet<Integer> c1, HashSet<Integer> c2) {
        HashSet<Integer> resultado = diferencia(union(c1, c2), interseccion(c1, c2));
        return resultado;
    }
    }
