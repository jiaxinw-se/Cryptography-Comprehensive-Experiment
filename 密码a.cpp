#include "oracle.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
unsigned char C_text[3][16] = 
{
  {159,11,19,148,72,65,168,50,178,66,27,158,175,109,152,54},
  {129,62,201,217,68,165,200,52,122,124,166,154,163,77,141,192},
  {223,112,227,67,196,0,10,42,227,88,116,206,117,230,76,49}
};
unsigned char C[32], M[48], Xor[16];
void E_function(int a) 
{
    int p, q, k, n;
    memset(C, 0, sizeof(C));
    for (p = 0; p < 16; ++i)
    {
        C[16 + p] = C_text[a][p];
    }
    for (p = 0; p < 16; ++p) 
    {
        for (q = 0; q < p; ++q)
        {
            C[15 - q] = Xor[15 - q] ^ (p + 1);
        }
        for (q = 0; q < 256; ++q) 
        {
            C[15 - p] = q;
            n = Oracle_Send(C, 2);
            if (n == 1) 
            {
                Xor[15 - p] = (q^(p + 1));
                M[16 * a + 15 - p]=(Xor[15 - p]^C_text[a - 1][15 - p]);
                break;
            }
        }
    }
}
int main(int argc, char* argv[]) 
{
    int i;
    Oracle_Connect();
    for (i = 1; i < 3; ++i)
    {
        E_function(i);
    }
    freopen("plaintext.txt", "w", stdout);
    for (i = 16; i < 48; ++i)
    {
        printf("%c", M[i]);
    }
    fclose(stdout);
    Oracle_Disconnect();
    return 0;
}
