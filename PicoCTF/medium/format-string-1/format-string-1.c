#include <stdio.h>
//checking for stack layout


int main() {
  char buf[1024];
  char secret1[64];
  char flag[64];
  char secret2[64];

  printf("%s%s%s%s", buf, secret1, flag, secret2);
  return 0;
}
