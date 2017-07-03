const char data[] =
"#include <stdio.h>\n"
"\n"
"int main() {\n"
"  unsigned int i;\n"
"\n"
"  printf(\"const char data[] =\");\n"
"  printf(\"\\n\");\n"
"  printf(\"\\\"\");\n"
"  for (i = 0; data[i]; i++) {\n"
"    switch (data[i]) {\n"
"      case '\\\\':\n"
"      case '\"':\n"
"        printf(\"\\\\%c\", data[i]);\n"
"        break;\n"
"      case '\\n':\n"
"        printf(\"\\\\n\");\n"
"        printf(\"\\\"\\n\\\"\");\n"
"        break;\n"
"      default:\n"
"        printf(\"%c\", data[i]);\n"
"    }\n"
"    if (!data[i + 1])\n"
"      printf(\"\\\"\");\n"
"  }\n"
"\n"
"  printf(\";\\n\\n\");\n"
"  for (i = 0; data[i]; i++)\n"
"    putchar(data[i]);\n"
"\n"
"  return 0;\n"
"}\n"
"";

#include <stdio.h>

int main() {
  unsigned int i;

  printf("const char data[] =");
  printf("\n");
  printf("\"");
  for (i = 0; data[i]; i++) {
    switch (data[i]) {
      case '\\':
      case '"':
        printf("\\%c", data[i]);
        break;
      case '\n':
        printf("\\n");
        printf("\"\n\"");
        break;
      default:
        printf("%c", data[i]);
    }
    if (!data[i + 1])
      printf("\"");
  }

  printf(";\n\n");
  for (i = 0; data[i]; i++)
    putchar(data[i]);

  return 0;
}
