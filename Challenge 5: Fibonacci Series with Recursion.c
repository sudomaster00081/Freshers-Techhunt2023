#include <stdio.h>

// Section 1 Function 
int fibonacci(int n);

int main() {
    int terms;

    // Section 2 Input
    printf("Enter the number of terms: ");
    scanf("%d", &terms);
    // Section 2 end

    // Section 3 Display Fibonacci 
    printf("Fibonacci Series: ");
    for (int i = 0; i < terms; i++) {
        printf("%d ", fibonacci(i));
    }
    // Section 3 end

    return 0;
}

// Section 4 Function
int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}
    // Section 4 end

// Fake Section 1
int fibonacci(int n) {
    if (n <= 0) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Fake Section 2
int fibonacci(int n) {
    if (n <= 1) {
        return 1;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}
