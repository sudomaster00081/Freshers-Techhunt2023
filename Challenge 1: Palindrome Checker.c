#include <stdio.h>
#include <string.h>

// Section 1 Libraries 
int isPalindrome(char str[]);

int main() {
    char input[100];
//section 1 end

    // Section 2 User Input
    printf("Enter a string: ");
    scanf("%s", input);
//section 2 end

    // Section 3 Palindrome Check
    if (isPalindrome(input)) {
        printf("Palindrome\n");
    } else {
        printf("Not a palindrome\n");
    }

    return 0;
}
//section 3 end

// Section 4 Palindrome Function
int isPalindrome(char str[]) {
    int left = 0;
    int right = strlen(str) - 1;
//section 4 end


    // Section 5 Palindrome Check Loop
    while (left < right) {
        if (str[left] != str[right]) {
            return 0; // Not a palindrome
        }
        left++;
        right--;
    }
    return 1; // Palindrome
}

//section 5 end

// Fake Section 1
int isPalindrome(char str[]) {
    int right = 0;
    int left = strlen(str) - 1;


// Fake Section 2
if (isPalindrome(input)) {
        printf("Not a Palindrome\n");
    } else {
        printf("Palindrome\n");
    }

    return 0;
}

