//Including all the required libararies
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

//Define a Byte as 8bits
typedef uint8_t BYTE;
 
//Main Method
int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        return 1;
    }
    char *file_name = argv[1]; // file_name storing the name of the file
    FILE *f = fopen(file_name, "r"); // Opening the file in readmode
    if (f == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }
    BYTE bytes[512];
    //reading 512bytes (block) from the memory card
    int img_count = 0;
    char *filename = malloc(sizeof(char) * 10);
    FILE *i;
    while (fread(bytes, sizeof(BYTE), 512, f) == 512)
    {
        if ((bytes[0] == 0xff) && (bytes[1] == 0xd8) && (bytes[2] == 0xff) && ((bytes[3] & 0xf0) == 0xe0))
        {
            //if it isn't the first time close old file here
            if (img_count == 0)
            {
                sprintf(filename, "%03i.jpg", img_count);
                i = fopen(filename, "w");
                fwrite(bytes, sizeof(BYTE), 512, i);
                img_count++;
            }
            else
            {
                fclose(i);
                sprintf(filename, "%03i.jpg", img_count);
                i = fopen(filename, "w");
                fwrite(bytes, sizeof(BYTE), 512, i);
                img_count++;
            }
        }
        else if (img_count == 0)
        {
            continue;
        }
        //write blocks into memory
        else
        {
            fwrite(bytes, sizeof(BYTE), 512, i);
        }
    }
    free(filename);
    fclose(i);
    // Close opened file
    fclose(f);
}
