#include <stdio.h>

int main(){
    int payment = 5000; //Δόση
    int total = 0; //Σύνολο 
    int i = 0;
    do{
        total+=payment;
        payment*=2;
        i++;
    } while (total <= 600000);
    printf("Goal will be reached in %d weeks",i);
    if(total>600000){
        printf("Left: %d",total-600000);
    }
    return 0;
}