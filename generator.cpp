#include <iostream>
#include <time.h>
int main()
{

    srand(time(NULL));
    int vv = 32769;
    int v = std::rand()%vv;
    bool b;
    for (int i = 0; i < 128; i++)
    {
        v = (v * 222 + 4)%vv;
        b = v % 2;
        std::cout << b;
    }

    return 0;
}
//01110011010101001111101001010100010100100001111001111100010001101011001111111110011100111001101110010011001111001100001100001101