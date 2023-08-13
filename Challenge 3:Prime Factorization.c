#include <stdio.h>

// Section 1: Function 
void primeFactors(int n);

int main() {
    int num;

    // Section 2 Input
    printf("Enter a number: ");
    scanf("%d", &num);
    // Section 2 end

    // Section 3 Factorization
    printf("Prime factors: ");
    primeFactors(num);
    // Section 3 end

    return 0;
}

// Section 4 Factorization Function
void primeFactors(int n) {
    for (int i = 2; i <= n; i++) {
        while (n % i == 0) {
            printf("%d ", i);
            n /= i;
        }
    }
   
}
 // Section 4 end


// Fake Section 1
void primeFactors(int n) {
    for (int i = 2; i >= n; i++) {
        while (n % j == 0) {
            printf("%d ", i);
            n /= i;
        }
    }
   
}


// Fake Section 2
void primeFactors(int n) {
    for (int i = 2; i <= n; i--) {
        while (n % i == 0) {
            printf("%d ", i);
            n /= i;
        }
    }
   
}