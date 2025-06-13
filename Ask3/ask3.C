#include <stdio.h>
#include <math.h>
float result = 0;
float func(float a,float b,float x) {
    if (x > 2) {
        result = (a+b)*x;
    }else if(x < -2) {
        if (a < b) {
            result = a;
        } else if(a > b) {
            result = b;
        } else {
            printf("Numbers are equal");
            result= a;
        }
    }else if (-2<=x && x<2){
        if (a < b) {
            result = b;
        } else if(a > b) {
            result = a;
        } else {
            printf("Numbers are equal");
            result= a;
        }        
    } else{
        result = fabs(a-b);
    }
    return result;
}

int main(){
    float x = 0;
    float a = 0;
    float b = 0;
    printf("Type x \n");
    scanf("%f",&x);
    printf("Type a \n");
    scanf("%f",&a);
    printf("Type b \n");
    scanf("%f",&b);   
    float result = func(a,b,x);
    printf("f(x) = %f",result);
    return 0;
}