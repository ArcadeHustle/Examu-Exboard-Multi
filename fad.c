// apt-get install binutils-mingw-w64-i686 g++-mingw-w64-i686 gcc-mingw-w64-i686
// i686-w64-mingw32-gcc fad.c -o fad.exe --static

#include <stdio.h>
#include <unistd.h>
#include <windows.h>

int main(int argc, char* argv[])
{
    printf("FuckA DarkSoft\n");

    FILE *fin;
    FILE *fout;
    int cur;
    int next;

    // if the trigger file exists lets rock out
    // read the current entry to start.
    if( access( "E:/fuckadarksoft", F_OK ) != -1 )
    {
    	fin = fopen("E:/fuckadarksoft", "r");
    	cur = fgetc(fin);
    	fclose(fin);
    }
    // if trigger file not present, write one. Set entry to 1 (0x31)
    // write base entry to start next boot on 2 (0x32)
    else
    {
        fout = fopen("E:/fuckadarksoft", "w");
        cur = 0x31;
        next=0x32;
        fputc(next,fout);
        fclose(fout);
    }


    // Override the round robbin boot process, force static entry
    if( access( "E:/fuckamitsutoo", F_OK ) != -1 )
    {
        fin = fopen("E:/fuckamitsutoo", "r");
        cur = fgetc(fin);
    }


    // Entry 1 (0x31)
    if(cur==0x31)
    {
        printf("Entry 1 - DB1");
        fout = fopen("E:/fuckadarksoft", "w");
        next=0x32;
        fputc(next,fout);
        fclose(fout);
        SetCurrentDirectory("C:");
        system("C:/DB1.exe");
    }
    // Entry 2 (0x32)
    else if(cur==0x32)
    {
        printf("Entry 2 - AH2");
        fout = fopen("E:/fuckadarksoft", "w");
        next=0x33;
        fputc(next,fout);
        fclose(fout);
        SetCurrentDirectory("D:");
        system("D:/AH2.exe");
    }
    // Entry 3 (0x33)
    else if(cur==0x33)
    {
        printf("Entry 3 - AH3");
        fout = fopen("E:/fuckadarksoft", "w");
        next=0x31;
        fputc(next,fout);
        fclose(fout);
        SetCurrentDirectory("E:");
        system("E:/AH30.exe");
    }
    // Sanity check on numeric range
    // set next boot to entry 2, and boot entry 1 if boot entry doesn't make sense. 
    else if( cur>0x33 || cur<0x31) 
    {
        printf("Catch All - DB1");
        fout = fopen("E:/fuckadarksoft", "w");
        cur = 0x31;
        next=0x32;
        fputc(next,fout);
        fclose(fout);
        SetCurrentDirectory("C:");
        system("C:/DB1.exe");
    }

}

