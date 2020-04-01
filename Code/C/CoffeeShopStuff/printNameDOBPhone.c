#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <string.h>

void DOB(){
//variables
//enum month{janurary,february,march,april,may,june,july,august,september,october,november,december};
char month[]="";
char day[]="";
char year[]="";
char DOB1[]="";

//user input
scanf("%s %s %s",&month,&day,&year);

//user check
if(strlen(month)>14){
    printf("No month associated with entered data\n");
    DOB();
}
else if(strlen(day)>2){
    int i;
    for(i=0;i<3;i++){
        if(day[i]>31){
            printf("You entered an incorrect day\n");
            DOB();
        }else{
            printf("Good entry\n");
        }
    }
    printf("You entered an incorrect day\n");
    DOB();
}else if(strlen(year)>4){
    printf("You entered an incorrect year\n");
    
}else{
    printf("Good entry\n");
}

}


char name(char nameFirst[20],char nameLast[20]){

//cat the two string into name

nameFirst[40] = (strcat(nameFirst,nameLast));
printf("%s\n", nameFirst);

return nameFirst;
}

void phone(){

}


int main()
{
    printf("Enter your first name then last name\n");
    char fname[20];
    char lname[20];
    char fullname[30] = "";
    
    scanf("%s %s",&fname,&lname);
    
    printf("%s",name(fname,lname));

    printf("Your name is: %s\n",fullname);


    //printf("Enter your date of birth in the follow format:Month Day Year: \n");
    //DOB();
    //printf("Enter your phone number\n");
    //phone();
    return 0;
}