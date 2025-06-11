/*
#Σε έναν αθλητικό διαγωνισμό άλματος εις ύψος συμμετείχαν 40 αθλητές παγκόσμιας φήμης. Από αυτούς προκρίθηκαν στον δεύτερο γύρο όσοι έκαναν επίδοση μεγαλύτερη απο 2.25 μ. 
#Να γραφεί αλγόριθμος ο οποίος: 
#α) Να διαβάζει την επίδοση κάθε αθλητή
#β) Να υπολογίζει το πλήθος και το ποσοστό αυτών που πέρασαν στον δεύτερο γύρο
#γ) Από αυτούς που προκρίθικαν στον δεύτερο γύρο, να εμφανίζει το ποσοστό αυτών που είχαν επίδοση μεγαλύτερη απο 2.3μ.
#Να μην γίνει έλεγχος τιμών εισόδου
*/

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