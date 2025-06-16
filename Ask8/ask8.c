#include <stdio.h>
#include <string.h>
#include <ctype.h>


float calc_cost(float time) { //Συνάρτηση για υπολογισμό κόστους
    float cost = 0.0;
    if (time <=3) {
        cost = time*2;
    } else if (time <=5) {
        cost = (2*3) + (time-3)*1.5;
    } else {
        cost = (2*3) + (2*1.5) + (time-5)*1.3;
    }
    return cost;
}

int main(){
    char plate [10]; //Αρ. Κυκλοφορίας
    float time = 0; //Ώρες στάθμευσης
    int i = 0; //Πλήθος οχημάτων με στάθμευση πανω από 2 ώρες
    while (1){ //ΔΕΝ ΕΦΑΡΜΟΖΕΤΑΙ ΣΕ ΓΛΩΣΣΑ
        printf("Enter licence plate no. (ABC - 1234) \n");
        fgets(plate, sizeof(plate), stdin);
        plate[strcspn(plate, "\n")] = '\0';
        if (strcmp(plate, "0") == 0){
            break; //ΔΕΝ ΕΦΑΡΜΟΖΕΤΑΙ ΣΕ ΓΛΩΣΣΑ
        }
        printf("Enter time (in hours) \n");
        scanf("%f",&time);
        while (time <= 0){
            printf("Error! time must be greater than 0! Try again \n");
            scanf("%f",&time);
        }
        if (time > 2){
            i++;
        }
        float price = calc_cost(time);
        printf("The vehicle with plate no. %s costs: %f€.",plate,price);
    }
    printf("Number of vehicles that parked for more than 2h: %d",i);
    return 0;
}
