#include<string>
#include<OAIDL.H>
#include<algorithm>

using namespace std;

//void SafeArrayAccessData()
//{
//	unsigned char* tempByte;
//	long UpperBounds, LowerBounds;
//	VARIANT &pData = pBarcode->Data;
//	SafeArrayGetLBound(pData.parray, 1, &LowerBounds);
//	SafeArrayGetUBound(pData.parray, 1, &UpperBounds);
//	SafeArrayAccessData(pData.parray, reinterpret_cast<void **>(&tempByte));
//	SafeArrayUnaccessData(pData.parray);
//	bcodeValue.strHexMessage = ToHexString(tempByte, UpperBounds);
//}

string ToHexString(unsigned char* bytes, long UpperBounds)
{
	string strHexResult;
	string strTempHexResult;
	for (size_t i = 0; i <= UpperBounds; i++, bytes++)
	{
		/*if (!(i % 16) && i)
		cout << endl;*/	// 16 char in a row
		char buf[10];
		sprintf_s(buf, "%02x", *bytes);
		strTempHexResult += buf;
		//cout << buf << " ";
	}
	transform(strTempHexResult.begin(), strTempHexResult.end(), back_inserter(strHexResult), ::toupper);
	//cout << endl;
	return strHexResult;
}