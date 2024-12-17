#include "helpers.h"
#include <math.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avarage =
                round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);

            image[i][j].rgbtRed = avarage;
            image[i][j].rgbtGreen = avarage;
            image[i][j].rgbtBlue = avarage;
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
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
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

int gx_calc(int x, int y, BYTE color)
{
    return color * (2 - abs(x)) * y;
}

int gy_calc(int x, int y, BYTE color)
{
    return color * (2 - abs(y)) * x;
}

int get_final_color(int gx, int gy)
{
    int value = round(sqrt(gx * gx + gy * gy));
    return value < 255 ? value : 255;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
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
            int gx_red = 0, gx_green = 0, gx_blue = 0;
            int gy_red = 0, gy_green = 0, gy_blue = 0;

            for (int x = -1; x <= 1; x++)
            {
                for (int y = -1; y <= 1; y++)
                {
                    int neighborRow = i + x, neighborCol = j + y;

                    BYTE red = copy[neighborRow][neighborCol].rgbtRed;
                    BYTE green = copy[neighborRow][neighborCol].rgbtGreen;
                    BYTE blue = copy[neighborRow][neighborCol].rgbtBlue;

                    if ((neighborRow >= 0 && neighborRow < height) &&
                        (neighborCol >= 0 && neighborCol < width))
                    {
                        gx_red += gx_calc(x, y, red);
                        gx_green += gx_calc(x, y, green);
                        gx_blue += gx_calc(x, y, blue);

                        gy_red += gy_calc(x, y, red);
                        gy_green += gy_calc(x, y, green);
                        gy_blue += gy_calc(x, y, blue);
                    }
                }
            }

            image[i][j].rgbtRed = get_final_color(gx_red, gy_red);
            image[i][j].rgbtGreen = get_final_color(gx_green, gy_green);
            image[i][j].rgbtBlue = get_final_color(gx_blue, gy_blue);
        }
    }
    return;
}
