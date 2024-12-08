#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and "
               "symbol\n");
    }
}

bool valid(string password)
{
    bool has_upper = false;
    bool has_lower = false;
    bool has_number = false;
    bool has_symbol = false;

    for (int i = 0; i < strlen(password); i++)
    {
        char character = password[i];

        if (isupper(character))
        {
            has_upper = true;
            continue;
        }
        else if (islower(character))
        {
            has_lower = true;
            continue;
        }
        else if (isdigit(character))
        {
            has_number = true;
            continue;
        }
        else if (ispunct(character))
        {
            has_symbol = true;
            continue;
        }
    }

    return (has_upper && has_lower && has_number && has_symbol);
}
