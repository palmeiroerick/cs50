#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int scrabble(char *word);

int main(void)
{
    int player1 = scrabble(get_string("Player 1: "));
    int player2 = scrabble(get_string("Player 2: "));

    if (player1 > player2)
    {
        printf("Player 1 wins!\n");
    }
    else if (player1 < player2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }

    return 0;
}

int scrabble(char *word)
{
    const int points_table[26] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                                  1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int sum = 0;

    for (int i = 0; i < strlen(word); i++)
    {
        int letter_id = toupper(word[i]) - 65;
        if (letter_id >= 0 && letter_id < 26)
        {
            sum += points_table[letter_id];
        }
    }

    return sum;
}
