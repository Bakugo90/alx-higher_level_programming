#include <stdio.h>
#include <string.h>

int main() {

  int *n, reverse = 0, remainder;
   n = 123;

  while (n != 0) {
    remainder = n % 10;
    reverse = reverse * 10 + remainder;
    n /= 10;

    int counted_number;
    counted_number = 3;
    if (strlen(reverse) == counted_number) {
        printf("%d ", reverse);
        counted_number = 0;
    }
  }

  printf("Reversed number = %d", reverse);

  return 0;
}