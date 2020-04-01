#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int i, a, b;
    string intSign = "";

    string numToWords[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    cin >> a;
    cin >> b;
    for (i = a;i <= 9; i++)
    {
        cout << numToWords[i-1] << endl;
    }
        
        if (9 < b)
        {
            for (i = 10; i <= b; i++)
            {

                if (i % 2 == 0)
                {
                    intSign += "even\n";
                }
                else
                {
                    intSign += "odd\n";
                }
            }
        }
    cout << intSign;
    return 0;
}