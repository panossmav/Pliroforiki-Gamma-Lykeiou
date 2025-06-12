
#include <stdio.h>

int main (){
    float perf = 0;
    int pass = 0;
    int pass_2 = 0; 
    for (int i = 0; i < 40;i++) {
        printf("Enter the distance of the jump \n");
        scanf("%f",&perf);
        if (perf > 2.25) {
            pass++;
            if (perf> 2.3) {
                pass_2++;
            }
        }
    }
    float pp1 = ((float)pass/40)*100;
    printf("%f percent of the candidates have passed. \n",pp1);
    if (pass!=0) {
        float pp2 = ((float)pass_2/pass)*100;
        printf("%f percent of the candidates that passed had a 2.3m or longer jump.",pp2);
    } else {
        printf("No one passed so no one jumped over 2.3m");
    }
    return 0;
}