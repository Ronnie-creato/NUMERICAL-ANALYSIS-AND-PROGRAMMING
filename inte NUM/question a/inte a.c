#include <stdio.h>
#include <math.h>

double regula(double a, double b, int iterations, double tol) {
    double fa = a * a - a - 2;
    double fb = b * b - b - 2;

    for (int i = 0; i < iterations; i++) {
        double x = (fa * b - fb * a) / (fa - fb);
        double fx = x * x - x - 2;
        
        if (fabs(fx) < tol) {
            return x;
        }
        if (fa * fx < 0) {
            b = x;
            fb = fx;
        } else {
            a = x;
            fa = fx;
        }
    }
    return -1;  // Indicate failure to converge
}

int main() {
    double a = 1, b = 3;
    int iterations = 1000;
    double tol = 1e-6;
    double root = regula(a, b, iterations, tol);

    if (root != -1) {
        printf("Root found: %f\n", root);
    } else {
        printf("Failed to find a root\n");
    }

    return 0;
}
