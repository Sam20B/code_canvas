#!bin/bash
#include <stdio.h>

int main()
{
    int a,b,c,currentyear;

    printf("what is your mother's age? ");
    scanf("%d",&a);

    printf("What is your father's age? ");
    scanf("%d",&b);

    printf("What is your age? ");
    scanf("%d",&c);

    printf("What year are you in? ");
    scanf("%d",&currentyear);

    int mothersbirthyear=currentyear-a;
    int fathersbirthyear=currentyear-b;
    int yourbirthyear=currentyear-c;

    printf("Your mother's year of birth is: %d\n",mothersbirthyear);

    printf("Your father's year of birth is: %d\n",fathersbirthyear);

    printf("Your year of birth is: %d\n",yourbirthyear);

}

