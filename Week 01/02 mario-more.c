#include <stdio.h>

void mario(int height);

int main(void) {
  mario(32);
  return 0;
}

void mario(int height) {
  for (int line = 1;line <= height; line++) {
    for (int space = height - line;space >= 1;space--) {
      printf(" ");
    }

    for (int hash = line;hash >= 1;hash--) {
      printf("#");
    }

    printf("  ");

    for (int hash = line;hash >= 1;hash--) {
      printf("#");
    }

    printf("\n");
  }
}
