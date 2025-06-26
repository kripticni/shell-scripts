#include <stdio.h>

int main(){
  volatile int a = 100;
  char str[100];
  scanf("%s",str);
  printf(str);
  printf("Value of A is: %i", a);
  return 0;
}
