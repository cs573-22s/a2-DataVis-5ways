public class Axis {
    final double domainMin;
    final double domainMax;
    final double rangeMin;
    final double rangeMax;

    Axis(double domainMin, double domainMax, double rangeMin, double rangeMax) {
        this.domainMin = domainMin;
         this.domainMax = domainMax;
         this.rangeMin = rangeMin;
         this.rangeMax = rangeMax;
    }

    double map(double x) {
        double px = (x - domainMin) / (domainMax - domainMin);
        return rangeMin + (rangeMax - rangeMin) * px;
    }
}
