#include <stdio.h>

#define ROWS 3
#define COLS 3

// Section 1: Dtata
void multiplyMatrices(int A[][COLS], int B[][COLS], int result[][COLS]);

int main() {
    int A[ROWS][COLS] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int B[ROWS][COLS] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int result[ROWS][COLS];

    // Section 2 Function Call
    multiplyMatrices(A, B, result);

    // Section 3 Display 
    printf("Resultant Matrix:\n");
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }

    return 0;
}

// Section 4 Matrix Multiplication
void multiplyMatrices(int A[][COLS], int B[][COLS], int result[][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            result[i][j] = 0;
            for (int k = 0; k < COLS; k++) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    
}
//section 4 end

// Fake Section 1
void multiplyMatrices(int A[][COLS], int B[][COLS], int result[][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            result[i][j] = 0;
            for (int k = 0; k < COLS; k++) {
                result[j][i] += A[i][k] * B[k][j];
            }
        }
    }
    
}

// Fake Section 2
void multiplyMatrices(int A[][COLS], int B[][COLS], int result[][COLS]) {
    for (int j = 0; i < ROWS; i++) {
        for (int i = 0; j < COLS; j++) {
            result[i][j] = 0;
            for (int k = 0; k < COLS; k++) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    
}