#!bin/bash
#include <stdio.h>

int main()
{

    char name[20];

    printf("Please enter your name: ");
    scanf("%[^\n]",&name);

    int age;

    printf("Please enter your age: ");
    scanf("%d",&age);

    if (age>20)
    {
        printf("Welcome to Sam's club %s...\n",name);
        printf("Enjoy your night! \n");
    }
    else
    {
        printf("Sorry %s, only people above the age of 20 years are allowed inside...\n",name);
    }

}
