#include<assert.h>
using namespace std;

char *strcpy(char *strDest, const char *strSrc)
{
	assert((strDest != NULL) && (strSrc != NULL));
	char* address = strDest;
	while ((*strDest++ = *strSrc++) != '\0');
	return address;
}

