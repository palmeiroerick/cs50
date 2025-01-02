#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *cipher(char *text, int key);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int key = atoi(argv[1]);

    string plaintext = get_string("plaintext:  ");
    string ciphertext = cipher(plaintext, key);
    printf("ciphertext: %s\n", ciphertext);

    return 0;
}

char *cipher(char *text, int key)
{
    for (int i = 0; i < strlen(text); i++)
    {
        if (isupper(text[i]))
        {
            text[i] = (text[i] - 65 + key) % 26 + 65;
        }
        if (islower(text[i]))
        {
            text[i] = (text[i] - 97 + key) % 26 + 97;
        }
    }

    return text;
}
