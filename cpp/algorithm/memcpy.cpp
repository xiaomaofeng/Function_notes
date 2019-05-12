void *memcpy(void *memDest, const void *memSrc, size_t size)
{
	assert((memDest != NULL) && (memSrc != NULL));
	char *addressSrc = (char *)memSrc;
	char *addressDest = (char *)memDest;
	if (memDest > (memSrc + size) || (memDest < memSrc))
	{
		while (size--)
			*addressDest++ = *addressSrc++;
	}
	else//overlap
	{
		addressDest += (size - 1);
		addressSrc += (size - 1);
		while(size--)
			*addressDest-- = *addressSrc--;
	}
	return memDest;
}