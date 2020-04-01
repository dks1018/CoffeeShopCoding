#include <iostream>
#include <cstdio>
#include <bits/stdc++.h>
using namespace std;


int max_of_four(int a, int b, int c, int d){
    int max;
    int numArray[4]={a,b,c,d};
    int n = sizeof(numArray)/sizeof(numArray[4]);

    std::sort(numArray,numArray+n);

    max=numArray[3];
    

    return max;
}


int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}