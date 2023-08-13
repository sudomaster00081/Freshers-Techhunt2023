#include <stdio.h>

// Section 1: Function 
int binarySearch(int arr[], int left, int right, int target);

int main() {
    int arr[] = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target;

    // Section 2  Input
    printf("Enter the target element: ");
    scanf("%d", &target);
    // Section 2 end

    // Section 3 Search
    int result = binarySearch(arr, 0, n - 1, target);

    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found\n");
    }
    // Section 3 end

    return 0;
}

// Section 4: Binary Search
int binarySearch(int arr[], int left, int right, int target) {
    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1; // Target not found
}
    // Section 4 end

// Fake Section 1
int binarySearch(int arr[], int left, int right, int target) {
    while (left < right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] > target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1; 
}

// Fake Section 2
int binarySearch(int arr[], int left, int right, int target) {
    if (arr[left] == target) {
        return left;
    } else if (arr[right] == target) {
        return right;
    } else {
        return -1;
    }
    
}
