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
    if( access( "E:/fuckadarksoft", F_OK ) != -1 )
    {
    	fin = fopen("E:/fuckadarksoft", "r");
    	cur = fgetc(fin);
    	fclose(fin);
    }
    else
    {
        fout = fopen("E:/fuckadarksoft", "w");
        cur = 0;
        next=1;
        fputc(next,fout);
        fclose(fout);
    }
    if(cur==0)
    {
        printf("Entry 0 - DB1");
        fout = fopen("E:/fuckadarksoft", "w");
        next=1;
        fputc(next,fout);
        fclose(fout);
        SetCurrentDirectory("C:");
        system("C:/DB1.exe");
    }
    else if(cur==1)
    {
        printf("Entry 1 - AH2");
        fout = fopen("E:/fuckadarksoft", "w");
        next=2;
        fputc(next,fout);
        fclose(fout);
        SetCurrentDirectory("D:");
        system("D:/AH2.exe");
    }
    else if(cur==2)
    {
        printf("Entry 2 - AH3");
        fout = fopen("E:/fuckadarksoft", "w");
        next=3;
        fputc(next,fout);
        fclose(fout);
        SetCurrentDirectory("E:");
        system("E:/AH30.exe");
    }
    else if(cur>2)
    {
        printf("Catch All (Entry 0) - DB1");
        fout = fopen("E:/fuckadarksoft", "w");
        next=1;
        fputc(next,fout);
        fclose(fout);
        SetCurrentDirectory("C:");
        system("C:/DB1.exe");
    }
    else
    {
        printf("Makes no sense cur is %x\n, Launch DB1",cur);
        SetCurrentDirectory("C:");
        system("C:/DB1.exe");
    }

}

