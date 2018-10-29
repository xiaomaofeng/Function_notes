#include <string>
#include<time.h>
using namespace std;

string GetCurrentTimeString()
{
	time_t timer;
	struct tm pTm;
	timer = time(NULL);
	localtime_s(&pTm,&timer);
	char szFileName[256] = { 0 };
	/*pTm->tm_mon;
	pTm->tm_mday;
	pTm->tm_hour;
	pTm->tm_min;
	pTm->tm_sec;*/
	sprintf_s(szFileName, "%d%02d%02d%02d%02d%02d", pTm.tm_year + 1900, pTm.tm_mon + 1, pTm.tm_mday, pTm.tm_hour, pTm.tm_min, pTm.tm_sec);
	string strTime = szFileName;
	return strTime;
}

//string GetCurrentTimeString()
//{
//	time_t timer;
//	struct tm* pTm;
//	timer = time(NULL);
//	pTm=localtime(&timer);
//	char szFileName[256] = { 0 };
//	pTm->tm_mon;
//	pTm->tm_mday;
//	pTm->tm_hour;
//	pTm->tm_min;
//	pTm->tm_sec;
//	sprintf_s(szFileName, "%d%02d%02d%02d%02d%02d", pTm->tm_year + 1900, pTm->tm_mon + 1, pTm->tm_mday, pTm->tm_hour, pTm->tm_min, pTm->tm_sec);
//	string strTime = szFileName;
//	return strTime;
//}
