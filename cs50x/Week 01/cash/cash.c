#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int cents = 0, coins = 0;

    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    while (cents >= 25)
    {
        cents -= 25;
        coins++;
    }

    while (cents >= 10)
    {
        cents -= 10;
        coins++;
    }

    while (cents >= 5)
    {
        cents -= 5;
        coins++;
    }

    while (cents >= 1)
    {
        cents -= 1;
        coins++;
    }

    printf("%d\n", coins);

    return 0;
}
