#include <iostream>
using namespace std;


int euclidean_algoritd(int a, int b)
{ 
    if(a%b== 0){ return b ;}
    else{return euclidean_algoritd(b,a%b);}
}

int main()
{
    cout << euclidean_algoritd(1053,234)<< endl;
    return 0;
}