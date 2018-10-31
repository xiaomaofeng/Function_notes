#include<string>
using namespace std;



string GetSuffix(string Name)
{
	size_t Pos = Name.rfind(".", Name.size()); //从后面开始寻找：rfind

	if (Pos == string::npos)
	{
		string SuffixStr;
		return SuffixStr;
	}
	else
	{
		string SuffixStr(Name.begin() + Pos, Name.end());
		return SuffixStr;
	}
}

