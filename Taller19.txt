public class Taller19 {
    public static void main(String[] args) {
        double sumaX = 0;
        double sumaY = 0;
        double Xpow = 0;
        double XxY = 0;
        double promX = 0;
        double promY = 0;
        double sy = 0;
        double syx = 0;
        double[] x = {0, 2, 4, 6, 8, 10, 12};
        double[] y = {0.1, 0.3, 0.8, 1.7, 2.7, 4.6, 6.8};
        double[] ypy = new double[x.length];
        double[] yaax = new double[x.length];
        double a = 0;
        double a1 = 0;
        double st = 0;
        double sr = 0;
        double r = 0;

        for (int i = 0; i < x.length; i++) {
            sumaX += x[i];
            sumaY += y[i];
            XxY += (x[i] * y[i]);
            Xpow = Xpow + Math.pow(x[i], 2);
            
        }

        promY = sumaY / x.length;
        promX = sumaX / x.length;

        for (int i = 0; i < x.length; i++) {
            ypy[i] = Math.pow((y[i] - promY), 2);
            
        }
        for (int i = 0; i < x.length; i++) {
            st += ypy[i];
        }
        System.out.println("Sumatoria X= " + sumaX);
        System.out.println("Sumatoria Y= " + sumaY);
        System.out.println("Xpow(2)= " + Xpow);
        System.out.println("Sumatoria X*Y= " + XxY);
        System.out.println("promX= " + promX);
        System.out.println("promY= " + promY);
        a1 = (x.length * (XxY) - (sumaX * sumaY)) / (x.length * (Xpow) - (Math.pow(sumaX, 2)));
        System.out.println("a1= " + a1);
        a = promY - (a1 * promX);
        System.out.println("a= " + a);

        for (int i = 0; i < x.length; i++) {
            yaax[i] = Math.pow(y[i] - a - a1 * x[i], 2);
        }
        for (int i = 0; i < x.length; i++) {
            sr += yaax[i];
        }
        System.out.println("St: " + st);
        System.out.println("Sr: " + sr);
        sy = Math.sqrt((st) / (x.length - 1));
        System.out.println("sy: " + sy);
        syx = Math.sqrt((sr) / (x.length - 2));;
        System.out.println("sy/x: " + syx);
        r = Math.sqrt((st - sr) / (st));
        System.out.println("r: " + r);
        r = r * 100;
        System.out.println("r: " + r + "%");
        System.out.println("y= " + a + " + " + a1 + "x");

    }
}
