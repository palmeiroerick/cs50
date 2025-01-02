#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height = 0;

    do
    {
        height = get_int("Height: ");
    }
    while (height <= 0);

    for (int line = 1; line <= height; line++)
    {
        for (int space = height - line; space >= 1; space--)
        {
            printf(" ");
        }
        for (int hash = line; hash >= 1; hash--)
        {
            printf("#");
        }
        printf("\n");
    }

    return 0;
}
