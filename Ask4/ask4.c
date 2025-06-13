#include <stdio.h>
#include <stdbool.h>
int main(){
    int h_p = 0; //Προϊόντα με τιμή μεγαλύτερη των 10€ 
    int sku = 1; //Κωδικός προϊόντος
    float price = 0; //Τιμή
    float quantity = 0; //Ποσότητα
    float cost = 0; //Κόστος
    do {
    printf("SKU: \n");
    scanf("%d", &sku);
    if (sku == 0){
        break;
    }
    printf("Price per item: \n");
    scanf("%f", &price);
    if (h_p > 10.00){
        h_p++;
    }
    printf("Quantity: \n");
    scanf("%f", &quantity);
    cost+=price;
    } while (true);
    printf("Cost: %f",cost);
    if (cost<=500){
        printf("Pay with cash \n");
    }else{
        int i =0; // Αριθμός δόσεων
        float loan = 0; //Ποσό δανείου
        int payment = 0; //Δόση δανείου
        do {
            payment=20+(5*i);
            loan+=payment;
            i++;
        }while(loan<cost);
        printf("Can be paid in %d installments",i+1);
    }
    printf("Valued items over 10€ per item: %d",h_p);
    return 0;
}