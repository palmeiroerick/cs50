#include <stdio.h>

int cash(int cents);

int main(void) {
  printf("%d\n", cash(0));
  printf("%d\n", cash(1));
  printf("%d\n", cash(4));
  printf("%d\n", cash(5));
  printf("%d\n", cash(10));
  printf("%d\n", cash(15));
  printf("%d\n", cash(24));
  printf("%d\n", cash(25));
  printf("%d\n", cash(26));
  printf("%d\n", cash(70));
  printf("%d\n", cash(99));
  printf("%d\n", cash(113));
  return 0;
}

int cash(int cents) {
  int coins = 0;

  while (cents >= 25) {
    cents -= 25;
    coins++;
  }

  while (cents >= 10) {
    cents -= 10;
    coins++;
  }

  while (cents >= 5) {
    cents -= 5;
    coins++;
  }

  while (cents >= 1) {
    cents -= 1;
    coins++;
  }

  return coins;
}
