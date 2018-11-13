#include<string>
#include<io.h>
#include<direct.h>

using namespace std;

void CreateOutputFileDir(string strOutputFilePath)
{
	char* fileName = (char*)strOutputFilePath.c_str();
	//char* pDir;
	int pos = 0;
	while ((pos = strOutputFilePath.find('\\', pos)) != string::npos)
	{
		string subStr = strOutputFilePath.substr(0, pos);
		if (_access(subStr.c_str(), 6) == -1)  //判断文件有没有读写权限：00-文件是否存在，02——写权限 ，04——读权限， 06——读写权限			成功返回0，失败返回-1		
		{
			_mkdir(subStr.c_str());
		}
		pos++;
	}

}