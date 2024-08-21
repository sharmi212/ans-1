#include <stdio.h>

int main() {
    double data[] = { // Dataset values here };
    int n = sizeof(data) / sizeof(data[0]);

    // Initialize variables
    int maxima[n];
    int minima[n];
    int max_count = 0, min_count = 0;

    // Iterate through the dataset
    for (int i = 1; i < n - 1; i++) {
        if (data[i - 1] < data[i] && data[i] > data[i + 1]) {
            maxima[max_count++] = i;
        }
        if (data[i - 1] > data[i] && data[i] < data[i + 1]) {
            minima[min_count++] = i;
        }
    }

    // Print the indices of maxima and minima
    printf("Maxima indices: ");
    for (int i = 0; i < max_count; i++) {
        printf("%d ", maxima[i]);
    }
    printf("\n");

    printf("Minima indices: ");
    for (int i = 0; i < min_count; i++) {
        printf("%d ", minima[i]);
    }
    printf("\n");

    return 0;
}
