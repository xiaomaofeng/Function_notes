#include<ostream>
#include<string>
#include<sstream>
#include<fstream>
#include<io.h>
#include<windows.h>

using namespace std;

#define MaxLengthOfLength 1000

void FindLicense(string dir, const string LicenseMatchKey)
{
	//将文件以二进制的形式读入流
	ifstream FileInput(dir, ios::binary);
	ostringstream StringStream;
	StringStream << FileInput.rdbuf();
	FileInput.close();
    //将流中的数据导入FileBuf
	string FileBuf = StringStream.str();
	string MatchString = LicenseMatchKey;
	size_t pos = string::npos;
	size_t pos = string::npos;
	size_t sNowPos = 0;

	bool ChangeFlag = false;//文件是否需要修改标志位
	while ((pos = FileBuf.find(MatchString, sNowPos))!= string::npos)//寻找以"t0 或't0开头的字符串
	{
		string LicenseStr;
		string NewLic;
		size_t i = pos + 1;//将POS+1 跳过('或")
		for (; FileBuf[i] != '\''&&FileBuf[i] != '"'; ++i)
		{
			LicenseStr += FileBuf[i];
			if (LicenseStr.size() >= MaxLengthOfLength)
				break;//超过最大长度限制 判断为不是License
		}
		if ((FileBuf.size() > i) && (('\'' == FileBuf[i]) || ('"' == FileBuf[i])))//字符串以' "结尾的
		{
			int length = LicenseStr.size();
			//LicChange(LicenseStr, dir);
			FileBuf.erase(pos + 1, length);
			FileBuf.insert(pos + 1, LicenseStr);
			ChangeFlag = true;
		}
		sNowPos = pos + LicenseStr.size();
	}
	if (true == ChangeFlag)
	{
		SetFileAttributes(dir.c_str(), FILE_ATTRIBUTE_NORMAL);
		ofstream FileOutput(dir, ios::binary);
		FileOutput << FileBuf;
		FileOutput.close();

	}
}