//inluding math.h library for round() function 
#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;
            float average = (red + green + blue) / 3.0; //Calculating Average
            int avg = round(average);
            image[i][j].rgbtRed = avg; //Assigning New Values
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }       
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float red = .393 *  image[i][j].rgbtRed + .769 *  image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            float green = .349 *  image[i][j].rgbtRed + .686 *  image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            float blue = .272 *  image[i][j].rgbtRed + .534 *  image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;
            // Multiplying and storing it in a variable
            if (red > 255) // converting all values higher than 255 to 255
            {
                red = 255.0;
            }
            if (green > 255)
            {
                green = 255.0;
            }
            if (blue > 255)
            {
                blue = 255.0;
            }
            image[i][j].rgbtRed = round(red);
            image[i][j].rgbtGreen = round(green);
            image[i][j].rgbtBlue = round(blue);
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width / 2); j++)
        {
            int red = image[i][j].rgbtRed; //Swaping values using a temp variable
            int blue = image[i][j].rgbtBlue;
            int green = image[i][j].rgbtGreen;
            image[i][j].rgbtRed = image[i][width - j - 1].rgbtRed;
            image[i][j].rgbtBlue = image[i][width - j - 1].rgbtBlue;
            image[i][j].rgbtGreen = image[i][width - j - 1].rgbtGreen;
            image[i][width - j - 1].rgbtRed = red;
            image[i][width - j - 1].rgbtBlue = blue;
            image[i][width - j - 1].rgbtGreen = green;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float count = 0;
            float redSum = 0;
            float greenSum = 0;
            float blueSum = 0;

            for (int k = -1; k < 2; k++) //pixels above ,below and same line
            {
                for (int l = -1; l < 2; l++) //pixels left, right and center
                {
                    if ((i + k < 0) || (i + k > height - 1))
                    {
                        continue;
                    }
                    if ((j + l < 0) || (j + l > width - 1))
                    {
                        continue;
                    }

                    redSum += image[i + k][j + l].rgbtRed;
                    blueSum += image[i + k][j + l].rgbtBlue;
                    greenSum += image[i + k][j + l].rgbtGreen;
                    count++;
                }
            }
            copy[i][j].rgbtRed = round(redSum / count);
            copy[i][j].rgbtBlue = round(blueSum / count);
            copy[i][j].rgbtGreen = round(greenSum / count);
        }
    }
    for (int i = 0; i < height; i++) // recopying the stuff back to image final
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = copy[i][j].rgbtRed;
            image[i][j].rgbtBlue = copy[i][j].rgbtBlue;
            image[i][j].rgbtGreen = copy[i][j].rgbtGreen;
        }
    }
}
