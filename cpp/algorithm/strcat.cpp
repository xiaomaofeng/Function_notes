char* strcat(char* strDest, const char* strSrc)
{
	assert((strDest != NULL) && (strSrc != NULL));
	char* res = strDest;
	while (*strDest)
		strDest++;
	while ((*strDest++ = *strSrc++) != '\0');
	return res;
}