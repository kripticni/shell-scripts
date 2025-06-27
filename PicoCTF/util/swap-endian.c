#include <stdio.h>
#include <string.h>

void swap_endian(char* dst, char* src) {
    if (src[0] == '0' && (src[1] == 'x' || src[1] == 'X'))
        src += 2;

    char* src_end = src;
    while (*src_end != '\0') ++src_end;

    src_end -= 2;

    while (src_end >= src) {
        *dst = *src_end;
        *(dst + 1) = *(src_end + 1);
        src_end -= 2;
        dst += 2;
    }

    *dst = '\0';
}

int main(){
  char str[] = "0x4011a0";
  char rev[] = "0x4011a0";
  swap_endian(rev, str);
  puts(rev);
}
