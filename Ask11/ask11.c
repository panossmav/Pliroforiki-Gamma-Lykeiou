#include <stdio.h>

int main(){
    int store_code = 1; //Κωδικός καταστηματος
    int employees_num = 0; //Αριθμός εργαζομένων
    float income = 0; //Έσοδα εταιρείας
    float expense = 0; //Έξοδα εταιρείας
    int min = 0; //Ελαχιστοι εργαζόμενοι
    int min_code = 0; //Κωδικός καταστήματος με ελάχιστους υπαλλήλους
    int loss_store = 0; //Πλήθος καταστημάτων με ζημιά
    
    do {
        printf("Enter store code \n");
        scanf("%d",&store_code);
        if (store_code == 0){
            break; //Μη διαθέσιμο σε ΓΛΩΣΣΑ
        }
        printf("Enter amount of employees \n");
        scanf("%d",&employees_num);
        printf("Enter store income\n");
        scanf("%f",&income);
        printf("Enter expenses \n");
        scanf("%f",&expense);

        float pnl = income-expense;
        if (pnl > 0){
            float net_pnl=pnl-(pnl*0.22);

        }else{
            loss_store++;
        }
        


    } while (store_code !=0);

    return 0;
}