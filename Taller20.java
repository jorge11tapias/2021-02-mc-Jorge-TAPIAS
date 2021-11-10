
package taller20;
public class Taller20 {
    
    public static void main(String[] args) {
double sumaZ = 0;
        double Raizsy = 0;
        double sumPromY = 0;
        double st = 0;
        double sy = 0;
        double syx = 0;
        double re = 0;
        double sumaX = 0;
        double sumaY = 0;
        double Xpow = 0;
        double XxY = 0;
        double promX = 0;
        double promY = 0;
        double[] x = {2,4,6,8,10,12,14};
        double[] y = {0.6,1.5,3.5,6,9.8,14.5,19.5};
        //double[] z = {1.6, 3, 1.1, 1.2, 3.2, 3.3, 1.7, 0.1};
        double a = 0;
        double a1 = 0;
        double sr = 0;
        double Ypow = 0;
        double XxZ = 0;
        double YxZ = 0;
        double promZ = 0;
        double a2 = 0;
        double Xpow3=0;
        double Xpow4=0;
        double XpowxY = 0;

        for (int i = 0; i < x.length; i++) {
            sumaX += x[i];
            sumaY += y[i];
            //sumaZ += z[i];
            XxY += (x[i] * y[i]);
            Xpow = Xpow + Math.pow(x[i], 2);
            Ypow = Ypow + Math.pow(y[i], 2);
            Xpow3 = Xpow3 + Math.pow(x[i], 3);
            Xpow4 = Xpow4 + Math.pow(x[i], 4);
            XpowxY = (Xpow * y[i]);

            //XxZ += (x[i] * z[i]);
            //YxZ += (y[i] * z[i]);

        }

        System.out.println("Sumatoria X= " + sumaX);
        System.out.println("Sumatoria Y= " + sumaY);
        System.out.println("Xpow(2)= " + Xpow);
        System.out.println("Sumatoria X*Y= " + XxY);
        promY = sumaY / x.length;
        System.out.println("promY= " + promY);

        double[][] m1 = {{x.length, sumaX, Xpow},
        {sumaX, Xpow, Xpow3},
        {Xpow, Xpow3, Xpow4}};
        double[] res = {sumaY, XxY, XpowxY};

        System.out.println("matriz original");
        imprimirSistema(m1, res);

        for (int i = 0; i < m1.length; i++) {
            double pivote = m1[i][i];
            if (pivote == 0) {
                for (int l = i + 1; l < m1.length; l++) {
                    if (m1[l][i] != 0) {
                        double[] renglonAux = m1[i];
                        m1[i] = m1[l];
                        m1[l] = renglonAux;
                        double ValorAux = res[i];
                        res[i] = res[l];
                        res[l] = ValorAux;

                        pivote = m1[i][i];
                        break;
                    }
                }
            }

            if (pivote != 1) {
                for (int j = 0; j < m1[i].length; j++) {
                    m1[i][j] = m1[i][j] / pivote;
                }

                res[i] = res[i] / pivote;

                System.out.println("Pivoteo");
                imprimirSistema(m1, res);

            } else {
                System.out.println("No requiere pivoteo");
            }

            //reduccion
            for (int l = 0; l < m1.length; l++) {
                if (i != l) {
                    double multiplicador = m1[l][i];
                    for (int j = 0; j < m1[l].length; j++) {
                        m1[l][j] = m1[l][j] - multiplicador * m1[i][j];
                    }
                    
                        res[l] = res[l] - multiplicador * res[i];
                    

                }
            }
            System.out.println("Reduccion");
            imprimirSistema(m1, res);

        }
        imprimirSistema(m1, res);
        for (int i = 0; i < 1; i++) {

            a = res[i];

        }
        for (int i = 0; i < 2; i++) {

            a1 = res[i];

        }
        for (int i = 0; i < 3; i++) {

            a2 = res[i];

        }
        System.out.println("a0= " + a);
        System.out.println("a1= " + a1);
        System.out.println("a2= " + a2);
        for (int i = 0; i < x.length; i++) {

            double ope1 = y[i] - promY;
           st = st + Math.pow(ope1, 2);
           double ope2 = y[i]-a-a1*x[i]-a2*Xpow;
            sr = sr + Math.pow(ope2, 2);

        }
        System.out.println("st = " + st);
        System.out.println("sr = " + sr);
        double Raizr = ((st - sr) / (st));
        re = Math.pow(Raizr, 0.5);

        re = re * 100;
        System.out.println("r= " + re);
        System.out.println("y= " + a + " + " + a1 + "x + " + a2 + "x^2");

    }

    private static void imprimirSistema(double[][] a, double[] b) {
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                System.out.print(a[i][j] + "    ");
            }
            System.out.println("    " + b[i]);
        }

    }
}
