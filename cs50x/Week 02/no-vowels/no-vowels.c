#include <cs50.h>
#include <stdio.h>
#include <string.h>

char *replace(char *word);

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: ./no-vowel word\n");
        return 1;
    }

    printf("%s\n", replace(argv[1]));
}

char *replace(char *word)
{
    for (int i = 0; i < strlen(word); i++)
    {
        switch (word[i])
        {
            case 'a':
                word[i] = '6';
                break;
            case 'e':
                word[i] = '3';
                break;
            case 'i':
                word[i] = '1';
                break;
            case 'o':
                word[i] = '0';
                break;
            default:
                break;
        }
    }

    return word;
}
