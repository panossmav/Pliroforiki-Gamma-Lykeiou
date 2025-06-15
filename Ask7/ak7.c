#include <stdio.h>

int main(){
    float a [50];
    float b [50];
    float c [50];
    int i = 0;
    for (i = 0;i< 50;i++){
        printf("Enter number %d",i+1);
        scanf("%f",&a[i]);
    }
    for (i = 0;i< 50;i++){
        printf("Enter number %d",i+1);
        scanf("%f",&b[i]);
    }
    for (i = 0; i<50;i++){
        c [i] = a[i]+a[i];
        printf("%f",c[i]);
    }
    return 0;
}