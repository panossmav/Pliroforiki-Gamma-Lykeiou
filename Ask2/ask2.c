#include <string.h>
#include <stdio.h>

char name[100] = "None"; // Όνομα
char gender = 'B';       // Φύλο
float b_sugar = -1;      // Σάκχαρο
int b_s_boys = 0; //Αγόρια με σάκχαρο εκτός ορίων
int b_s_girls = 0; //Κορίτσια με σάκχαρο εκτός ορίων
int main() {
    for (int i = 1; i <= 90; i++) {
        do {
            printf("Enter the student's name \n");
            fgets(name, sizeof(name), stdin);
            int len = strlen(name);
            if (name[len - 1] == '\n') {
                name[len - 1] = '\0';
            }
            printf("Enter A for by or K for girl \n");
            scanf("%c",gender);
            printf("Enter blood sugar: /n");
            scanf("%f",&b_sugar);
        } while (gender != 'A' && gender != 'K' && b_sugar > 0);
        if (b_sugar > 110 || b_sugar <70) {
            printf("%s %s %f Abnormal Blood Sugar \n",name,gender,b_sugar);
            if (gender == 'A') {
                b_s_boys++;
            }else {
                b_s_girls++;
            }
        }
    }
    printf("Boys with abnormal blood sugar: %d \n",b_s_boys);
    printf("Girls with abnormal blood sugar: %d \n",b_s_girls);
    return 0;
}
