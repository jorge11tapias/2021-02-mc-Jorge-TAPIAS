public class Taller21 {

    public static void main(String[] args) {
        double[] x = {1, 1, 2, 3, 1, 2,3,3};
		        double[] xx = {-1, 0, 0, 1, 1, 2,2,0};
		        double[] y = {1.6, 3, 1.1, 1.2, 3.2, 3.3,1.7,0.1};
		        double sumaX = 0;
		        double sumaXX = 0;
		        double sumaY = 0;
		        double sumaxy = 0;
		        double[] xpow2 = new double[x.length];
		        double sumaxpow2 = 0;
		        double[] xxpow2 = new double[x.length];
		        double sumaxxpow2 = 0;
		        double[] xxx = new double[x.length];
		        double sumaxxx = 0;
		        double[] xy = new double[x.length];
		        double[] xxy = new double[x.length];
		        double sumaxxy = 0;
		        double[] ypypow2 = new double[x.length];
		        double sumaypypow2 = 0;
		        double sy = 0;
		        double promY = 0;
		        double promX = 0;
		        double syx = 0;

		        double[] ya0a1xa2xxpow2 = new double[x.length];
		        double sumaya0a1xa2xxpow2=0;
		        double[] yaax = new double[x.length];

		        double a0 = 0;
		        double a1 = 0;
		        double a2 =0;
		        double r = 0;
		       
		       

		        for (int i = 0; i < x.length; i++) {
		            sumaX += x[i];
		            sumaXX += xx[i];
		            sumaY += y[i];
		        }
		        promY = sumaY / y.length;
		        promX = sumaX / x.length;
		        for (int i = 0; i < x.length; i++) {

		            xxx[i] = x[i] * xx[i];
		            xpow2[i] = Math.pow(x[i], 2);
		            xxpow2[i] = Math.pow(xx[i], 2);
		            xy[i] = x[i] * y[i];
		            xxy[i] = xx[i] * y[i];
		            ypypow2[i] = Math.pow((y[i] - promY), 2);
		        }

		        for (int i = 0; i < x.length; i++) {
		            sumaypypow2 += ypypow2[i];
		            sumaxpow2 += xpow2[i];
		            sumaxxpow2 += xxpow2[i];
		            sumaxxx += xxx[i];
		            sumaxxy += xxy[i];
		            sumaxy += xy[i];

		        }
		        System.out.println(" sumaypypow2: " + sumaypypow2 + " sumaxpow2:  " + sumaxpow2 + " sumaxxpow2: " + sumaxxpow2);
		        System.out.println("sumaxxx: " + sumaxxx + " sumaxxy:  \n" + sumaxxy + " sumaxy: \n" + sumaxy +"sumax " +sumaX + "sumaY "+sumaY+ "sumaxx "+ sumaXX);

		       
		         double[][] a = {{x.length, sumaX, sumaXX},
		        {sumaX, sumaxpow2, sumaxxx}, {sumaXX, sumaxxx, sumaxxpow2}

		        };
		        double[] b = {sumaY, sumaxy, sumaxxy};
		        System.out.println("Matriz Original");
		        imprimirSistema(a, b);
		        for (int i = 0; i < a.length; i++) {
		            double pivote = a[i][i];
		            if (pivote == 0) {
		                for (int m = i + 1; m < a.length; m++) {
		                    if (a[m][i] != 0) {
		                        double[] renglonAux = a[i];
		                        a[i] = a[m];
		                        a[m] = renglonAux;

		                        double valorAux = b[i];
		                        b[i] = b[m];
		                        b[m] = valorAux;

		                        pivote = a[i][i];
		                        break;
		                    }
		                }
		                System.out.println("Cambio de renglón");
		                imprimirSistema(a, b);
		            }
		            if (pivote != 1) {
		                for (int j = 0; j < a[i].length; j++) {
		                    a[i][j] = a[i][j] / pivote;

		                }
		                b[i] = b[i] / pivote;
		                System.out.println("Pivoteo");
		                imprimirSistema(a, b);

		            } else {
		                System.out.println("No requiere Pivoteo");
		            }

		            for (int l = 0; l < a.length; l++) {
		                if (i != l) {
		                    double multiplicador = a[l][i];
		                    for (int j = 0; j < a[l].length; j++) {
		                        a[l][j] = a[l][j] - multiplicador * a[i][j];
		                    }
		                    b[l] = b[l] - multiplicador * b[i];
		                }
		            }
		            System.out.println("Reduccion");
		            imprimirSistema(a, b);
		        }
		        for (int i = 0; i < b.length; i++) {
		        	a0=b[0];
			        a1=b[1];
			        a2 = b[2];
				}
		        for (int i = 0; i < x.length; i++) {
		        	ya0a1xa2xxpow2[i]=Math.pow((y[i]-a0-a1*x[i]-a2*xx[i]), 2);
				}
		        for (int i = 0; i < x.length; i++) {
		        	sumaya0a1xa2xxpow2+=ya0a1xa2xxpow2[i];
				}
		        System.out.println("a0: "+ a0 +" a1: "+ a1+" a2: " + a2);
		        System.out.println("st: "+sumaypypow2);
		        System.out.println("sr: "+ sumaya0a1xa2xxpow2);
		        r = Math.sqrt((sumaypypow2 - sumaya0a1xa2xxpow2) / (sumaypypow2));
		        System.out.println("r= " +r);
		        r=r*100;
		        System.out.println("r= " +r + "%");
		        System.out.println("z= " + a0 +" +" + a1 + "x +" +a2 + "y");
		       

		    }

		    public static void imprimirSistema(double[][] a, double[] b) {
		        for (int i = 0; i < a.length; i++) {
		            for (int j = 0; j < a[i].length; j++) {
		                System.out.print(a[i][j] + " ");
		            }
		            System.out.println("   " + b[i]);
		        }
		    }
		}
