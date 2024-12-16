#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            BYTE average =
                round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // BYTE average = round((image[i][j].rgbtRed + image[i][j].rgbtGreen +
            // image[i][j].rgbtBlue) / 3.0);
            BYTE red = image[i][j].rgbtRed;
            BYTE green = image[i][j].rgbtGreen;
            BYTE blue = image[i][j].rgbtBlue;

            int sepia_red = round(0.393 * red + 0.769 * green + 0.189 * blue);
            int sepia_green = round(0.349 * red + 0.686 * green + 0.168 * blue);
            int sepia_blue = round(0.272 * red + 0.534 * green + 0.131 * blue);

            image[i][j].rgbtRed = sepia_red > 255 ? 255 : sepia_red;
            image[i][j].rgbtGreen = sepia_green > 255 ? 255 : sepia_green;
            image[i][j].rgbtBlue = sepia_blue > 255 ? 255 : sepia_blue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][width - j - 1];
            image[i][width - j - 1] = image[i][j];
            image[i][j] = temp;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {

            int red_average = 0, green_average = 0, blue_average = 0, count = 0;

            for (int x = -1; x <= 1; x++)
            {
                for (int y = -1; y <= 1; y++)
                {
                    int neighborRow = i + x, neighborCol = j + y;

                    if ((neighborRow >= 0 && neighborRow < height) &&
                        (neighborCol >= 0 && neighborCol < width))
                    {
                        red_average += copy[neighborRow][neighborCol].rgbtRed;
                        green_average += copy[neighborRow][neighborCol].rgbtGreen;
                        blue_average += copy[neighborRow][neighborCol].rgbtBlue;
                        count++;
                    }
                }
            }

            red_average = round((float) red_average / count);
            green_average = round((float) green_average / count);
            blue_average = round((float) blue_average / count);

            image[i][j].rgbtRed = red_average;
            image[i][j].rgbtGreen = green_average;
            image[i][j].rgbtBlue = blue_average;
        }
    }

    return;
}
