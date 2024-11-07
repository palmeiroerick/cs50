#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

char *cipher(char *text, char *key);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    string key = argv[1];

    for (int i = 0; i < strlen(key); i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }
    }

    if (strlen(key) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    int freq[26] = {0};

    for (int i = 0; i < strlen(key); i++)
    {
        key[i] = toupper(key[i]);
        int letter = key[i] - 65;
        freq[letter]++;
        if (freq[letter] > 1)
        {
            printf("Key must contain each letter exactly once.\n");
            return 1;
        }
    }

    string plaintext = get_string("plaintext:  ");
    string ciphertext = cipher(plaintext, key);
    printf("ciphertext: %s\n", ciphertext);

    return 0;
}

char *cipher(char *text, char *key)
{
    for (int i = 0; i < strlen(text); i++)
    {
        if (!isalpha(text[i]))
            continue;
        char key_char = key[isupper(text[i]) ? text[i] - 65 : text[i] - 97];
        text[i] = isupper(text[i]) ? key_char : key_char + 32;
    }

    return text;
}
