package parcial1;

import java.util.HashSet;

public class parcial1 {
    
//CONJUNTO B PARCIAL
    public static void main(String[] args) {
        HashSet<Integer> B = new HashSet<>();
        for (int i = 5; i <= 24; i++) {
            B.add(i);
        }

        //Conjunto C PARCIAL
        HashSet<Integer> C = new HashSet<>();
        for (int i = 1; i <= 29; i++) {
            if (i % 3 == 1) {
                C.add(i);
            }
        }
        //Conjunto A PARCIAL
        HashSet<Integer> A = new HashSet<>();
        A.add(1);
        A.add(3);
        A.add(5);
        A.add(7);
        A.add(11);
        A.add(22);
        A.add(44);

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
        D.add(47);

//Operación 1
        HashSet<Integer> O1 = diferencia(interseccion(A, D),diferenciasimetrica(B,C));
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
