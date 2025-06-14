#include <stdio.h>
#include <math.h>

int main(){
    int numbers[250];
    int odd = 0; //Άρτιοι
    int even = 0; //Περιττοί
    for (int i = 1; i<=250;i++){
        printf("Type a number \n");
        scanf("%d",&numbers[i]);
        if (numbers[i] % 2 == 1){
            odd++;
        } else {
            even++;
        }
    }
    float p_odd = (odd/250)*100;
    float p_even = (even/250)*100;
    printf("Odd: %f%% \n Even: %f%%",p_odd, p_even);
    return 0;
}