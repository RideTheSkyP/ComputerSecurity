#include <stdio.h>
#include <string.h>

int auth(char *code)
{
    int ret, cmp;
    cmp = strcmp(code, "haslo");
    if (cmp == 0)
    {
        ret = 1;
    }
    else
    {
        ret = 0;
    }
    return ret;
}

void login(char *code)
{
    int secret = 9;
    int authenticated = auth(code);
    char pass[10];
    strcpy(pass, code);
    if (authenticated)
    {
        printf("The secret is: %d\n", secret);
    }
    else
    {
        printf("Unauthorized\n");
    }
}

int main(int argc, char *argv[])
{
    char code[10];
    strcpy(code, argv[1]);
    login(code);
    return 0;
}
