#include <stdio.h>

int main(){
  int header[] = { 16, 9, 3, 15, 3, 20, 6 };
  int trailer[] = { 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14 };

  const int n = sizeof(header)/sizeof(int);
  const int m = sizeof(trailer)/sizeof(int);

  int i;
  for(i = 0; i < n; ++i)
    printf("%c", (header[i] + 'a' - 1));
  printf("{");
  for(i = 0; i < m; ++i)
    printf("%c", (trailer[i] + 'a' - 1));
  printf("}");
  return 0;
}
