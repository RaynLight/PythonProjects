#include<stdio.h>
#include<stdlib.h>


int main(int argc, char* argv[]){

        if(argc!=2){
                printf("PLEASE enter input file\n");
                return 1;
        }
        char* file_name = argv[1];

        FILE* file = fopen(file_name,"r"); 



        long long counter = 0; 

        while(!feof(file)){
                char byte = fgetc(file);
                printf("%x",byte);
                counter++;


                if(counter%16==0){
                        printf("\n");
                }
        }









        fclose(file);







}

