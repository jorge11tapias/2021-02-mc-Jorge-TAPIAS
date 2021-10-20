package taller14;

/**
Presentado por : Jorge Enrique Tapias
 */
public class Taller14 {

    public static void main(String[] args) {
        double[][] a = {{2, 2, 0},
        {3, 3, 4},
        {4, 0, 1}};
        double[] b = {6, 9, 8};
        System.out.println("Matriz original");
        imprimirSistema(a, b);
        for (int i = 0; i < a.length; i++) {
            double pivote = a[i][i];
            if(pivote == 0){
                for (int l = i + 1 ; l <a.length; l++){
                    if(a[l][i] !=0){
                        double[] renglonAux = a[i];
                        a[i] = a[l];
                        a[l] = renglonAux;
                        double ValorAux = b[i];
                        b[i]= b[l];
                        b[l]= ValorAux;
                        
                        pivote = a[i][i];
                        break;
                    }
                }
            }
            
            if (pivote != 1) {
                for (int j = 0; j < a[i].length; j++) {
                    a[i][j] = a[i][j] / pivote;
                }
                b[i] = b[i] / pivote;
                System.out.println("Pivoteo");
                imprimirSistema(a, b);
            } else {
                System.out.println("No requiere pivoteo");
            }
            
            //reduccion
            for (int l = 0; l <a.length ; l++){
                if( i != l){
                    double multiplicador = a[l][i];
                    for (int j = 0; j<a[l].length; j++){
                        a[l][j] = a[l][j] - multiplicador * a[i][j];
                    }
                    b[l] = b[l] - multiplicador * b[i];
                }
            }
            System.out.println("Reduccion");
            imprimirSistema (a, b);
        }
    }

    private static void imprimirSistema(double[][] a, double[] b) {
        for (int i = 0; i < a.length ; i++) {
            for (int j = 0; j <a[i].length ; j++) {
                System.out.print(a[i][j] + "    ");
            }
            System.out.println("    " + b[i]);
        }

    }
}
