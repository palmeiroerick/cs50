#include <cs50.h>
#include <stdio.h>

int main()
{
    int sum = 0, digits = 0;
    long number, starts;
    number = starts = get_long("Number: ");

    while (starts >= 100)
    {
        starts /= 10;
    }

    while (number)
    {
        // last number
        int product = number % 10;
        sum += product;

        number = number / 10;
        digits++;

        // second last
        if (number)
        {
            product = number % 10 * 2;

            if (product >= 10)
            {
                sum += product % 10;
                product /= 10;
            }

            sum += product;

            number = number / 10;
            digits++;
        }
    }

    if (sum % 10 == 0)
    {
        if (digits == 15 && (starts == 34 || starts == 37))
        {
            printf("AMEX\n");
        }
        else if (digits == 16 && (starts >= 51 && starts <= 55))
        {
            printf("MASTERCARD\n");
        }
        else if ((digits == 13 || digits == 16) && (starts >= 40 && starts <= 49))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }

    return 0;
}
