#include <stdio.h>

float max(float a,float b,float c){
    float max = -9999999;
    if (a > max){
        max = a;
    }
    if (b > max){
        max = b;
    }
    if (c > max){
        max = c;
    }
    return max;
}

int main(){
    float x = 0;
    float y = 0;
    float z = 0;
    printf("Type x \n");
    scanf("%f",&x);
    printf("Type y \n");
    scanf("%f",&y);
    printf("Type z \n");
    scanf("%f",&z);   
    float result = max(x,y,z);
    printf("Max: %f",result);
    return 0;

}