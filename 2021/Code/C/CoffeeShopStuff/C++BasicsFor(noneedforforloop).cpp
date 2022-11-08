#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a,b;
    //scanf("%d %d",&a,&b);
for(int i = 1;i<2;i++){
    scanf("%d%d",&a,&b);
    if(1<=a && a <=9){
        switch(a){
            case 1: printf("one\n");
            break;
            case 2: printf("two\n");
            break;
            case 3: printf("three\n");
            break;
            case 4: printf("four\n");
            break;
            case 5: printf("five\n");
            break;
            case 6: printf("six\n");
            break;
            case 7: printf("seven\n");
            break;
            case 8: printf("eight\n");
            break;
            case 9: printf("nine\n");
            break;
        }
    }else{
        printf("Greater than 9\n");
    }
    if(1<=b && b <=9){
        switch(b){
            case 1: printf("one");
            break;
            case 2: printf("two");
            break;
            case 3: printf("three");
            break;
            case 4: printf("four");
            break;
            case 5: printf("five");
            break;
            case 6: printf("six");
            break;
            case 7: printf("seven");
            break;
            case 8: printf("eight");
            break;
            case 9: printf("nine");
            break;
        }
    }else{
        printf("Greater than 9");
    }if(a%2==0){
        printf("\neven");

    }else{printf("\nodd");}
    if(b%2==0){
        printf("\neven");

    }else{printf("\nodd");}
}
    return 0;
}
