#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(char *text);
int count_words(char *text);
int count_sentence(char *text);

int main(void)
{
    string text = get_string("Text: ");

    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentence(text);

    int index = round(0.0588 * ((float) letters / words * 100) -
                      0.296 * ((float) sentences / words * 100) - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index < 16)
    {

        printf("Grade %d\n", index);
    }
    else
    {
        printf("Grade 16+\n");
    }

    return 0;
}

int count_letters(char *text)
{
    int letters = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (toupper(text[i]) >= 65 && toupper(text[i]) < 91)
        {
            letters++;
        }
    }

    return letters;
}

int count_words(char *text)
{
    int words = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if ((text[i] == 32 && text[i - 1] != 32) || (i == strlen(text) - 1 && text[i] != 32))
        {
            words++;
        }
    }

    return words;
}

int count_sentence(char *text)
{
    int sentences = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            sentences++;
        }
    }

    return sentences;
}
