#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");

    if (card == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    FILE *img = NULL;
    int file_count = 0;
    uint8_t buffer[BLOCK_SIZE];

    while (fread(buffer, 1, BLOCK_SIZE, card) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            if (img != NULL)
            {
                fclose(img);
            }

            char filename[8];
            sprintf(filename, "%03i.jpg", file_count);

            img = fopen(filename, "w");

            if (img == NULL)
            {
                printf("Could not open file.\n");
                fclose(card);
                return 1;
            }

            fwrite(buffer, 1, BLOCK_SIZE, img);

            file_count++;
        }
        else
        {
            if (img != NULL)
            {
                fwrite(buffer, 1, BLOCK_SIZE, img);
            }
        }
    }

    if (img != NULL)
    {
        fclose(img);
    }

    fclose(card);

    return 0;
}
