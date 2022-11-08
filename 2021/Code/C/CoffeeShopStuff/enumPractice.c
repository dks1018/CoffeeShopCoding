#include <stdio.h>
#include <stdlib.h>

int main()
{
    enum month {jan=1,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec};

    int userBirth;
    //enum month userEnter;

     printf("What what month is your birthday? (number 1-12)\n");
     scanf("%d",&userBirth);

       int num;
        switch(userBirth)
        {
            case 1: userBirth = jan;
                enum month userEnter = userBirth;
            break;
            case 2: userBirth = feb;
                
            break;
            case 3: userBirth = mar;
            break;
            case 4: userBirth = apr;
            break;
            case 5: userBirth = may;
            break;
            case 6: userBirth = jun;
            break;
            case 7: userBirth = jul;
            break;
            case 8: userBirth = aug;
            break;
            case 9: userBirth = sep;
            break;
            case 10: userBirth = oct;
            break;
            case 11: userBirth = nov;
            break;
            case 12: userBirth = dec;
            break;
            
        }
        printf("%d",userEnter[num]);
    return 0;
}