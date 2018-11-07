#include<vector>
#include<string>
#include<fstream>
#include<iostream>
#include"rapidjson/document.h"
#include"rapidjson/istreamwrapper.h"
#include"rapidjson/stringbuffer.h"
#include"rapidjson/writer.h"

#include"logger/logger.h"
using namespace LOGGER;
using namespace rapidjson;
using namespace std;

CLogger logger(LogLevel_Info, CLogger::GetAppPathA().append("log\\"));
int LightLog = 0;

void IfstreamJson()
{
	bool bInitNormal;			//初始化状态 True=Normal
	string s7zExecPath;				//7z.exe的目录
	string GzipExecPath;			//gzip.exe的目录
	vector<string> sZIPPackFileList;	//必定存在压缩包的具体目录
	vector<string> sTARPackFileList;	//必定存在压缩包的具体目录
	vector<string>	sFileDir;		//可能包含文件的目录 不需要解压缩包
	vector<string>	sPackageDir;//包可能存在的目录
	vector<string> sLicenseMatchKey;//License适配关键字
	vector<string> sFileType;	//支持自动替换的文件类型

	ifstream fJsonFile(CLogger::GetAppPathA().append("\\") + "init.json");
	logger.TraceInfo("	Open init.json.	");

	IStreamWrapper iStreamWrap(fJsonFile);
	Document Document;
	Document.ParseStream(iStreamWrap);

	//获取初始化基本信息
	//-------------------------------------------------------------------------------------
	if (Document.HasMember("LightLog"))
	{
		LightLog = atoi(Document["LightLog"].GetString());
		logger.TraceInfo("	Import Param [LightLog]=%d.	", LightLog);
	}
	else
	{
		logger.TraceWarning("	init.json have not Param[LightLog].	");
		bInitNormal = FALSE;
		return;
	}
	//-------------------------------------------------------------------------------------	
	if (Document.HasMember("7zExecPath"))
	{
		s7zExecPath = Document["7zExecPath"].GetString();
		logger.TraceInfo("	Import Param [7zExecPath]=%s.	", s7zExecPath.c_str());
	}
	else
	{
		logger.TraceWarning("	init.json have not Param[7zExecPath].	");
		bInitNormal = FALSE;
		return;
	}
	//-------------------------------------------------------------------------------------
	if (Document.HasMember("GzipExecPath"))
	{
		GzipExecPath = Document["GzipExecPath"].GetString();
		logger.TraceInfo("	Import Param [GzipExecPath]=%s.	", GzipExecPath.c_str());
	}
	else
	{
		logger.TraceWarning("	init.json have not Param[GzipExecPath].	");
		bInitNormal = FALSE;
		return;
	}
	//-------------------------------------------------------------------------------------	
	if (Document.HasMember("sLicenseMatchKey"))
	{
		if (Document["sLicenseMatchKey"].IsArray())
		{
			for (size_t i = 0; i < Document["sLicenseMatchKey"].Size(); ++i)
			{
				sLicenseMatchKey.push_back(Document["sLicenseMatchKey"][i].GetString());
				logger.TraceInfo("	Import Param [sLicenseMatchKey]=%s.", sLicenseMatchKey[i].c_str());
			}
		}
		else
		{
			logger.TraceWarning("init.json have not Param[sLicenseMatchKey].");
			bInitNormal = FALSE;
			return;
		}
	}
	//-------------------------------------------------------------------------------------
	if (Document.HasMember("sPackageDir"))
	{
		if (Document["sPackageDir"].IsArray())
		{
			for (size_t i = 0; i < Document["sPackageDir"].Size(); ++i)
			{
				sPackageDir.push_back(Document["sPackageDir"][i].GetString());
				logger.TraceInfo("	Import Param [sPackageDir]=%s.	", sPackageDir[i].c_str());
			}
		}
		else
		{
			logger.TraceWarning("	init.json have not Param[sPackageDir].	");
			return;
		}
	}
	//-------------------------------------------------------------------------------------
	if (Document.HasMember("sFileDir"))
	{
		if (Document["sFileDir"].IsArray())
		{
			for (size_t i = 0; i < Document["sFileDir"].Size(); ++i)
			{
				sFileDir.push_back(Document["sFileDir"][i].GetString());
				logger.TraceInfo("	Import Param [sFileDir]=%s.	", sFileDir[i].c_str());
			}
		}
		else
		{
			logger.TraceWarning("	init.json have not Param[sFileDir].	");
			return;
		}
	}
	//-------------------------------------------------------------------------------------
	if (Document.HasMember("sZIPPackFileList"))
	{
		if (Document["sZIPPackFileList"].IsArray())
		{
			for (size_t i = 0; i < Document["sZIPPackFileList"].Size(); ++i)
			{
				sZIPPackFileList.push_back(Document["sZIPPackFileList"][i].GetString());
				logger.TraceInfo("	Import Param [sZIPPackFileList]=%s.	", sZIPPackFileList[i].c_str());
			}
		}
		else
		{
			logger.TraceWarning("	init.json have not Param[sZIPPackFileList].	");
			return;
		}
	}
	//-------------------------------------------------------------------------------------
	if (Document.HasMember("sTARPackFileList"))
	{
		if (Document["sTARPackFileList"].IsArray())
		{
			for (size_t i = 0; i < Document["sTARPackFileList"].Size(); ++i)
			{
				sTARPackFileList.push_back(Document["sTARPackFileList"][i].GetString());
				logger.TraceInfo("	Import Param [sTARPackFileList]=%s.	", sTARPackFileList[i].c_str());
			}
		}
		else
		{
			logger.TraceWarning("	init.json have not Param[sTARPackFileList ].	");
			return;
		}
	}
	//-------------------------------------------------------------------------------------
	if (Document.HasMember("sFileType"))
	{
		if (Document["sFileType"].IsArray())
		{
			for (size_t i = 0; i < Document["sFileType"].Size(); ++i)
			{
				sFileType.push_back(Document["sFileType"][i].GetString());
				logger.TraceInfo("	Import Param [sFileType]=%s.	", sFileType[i].c_str());
			}
		}
		else
		{
			logger.TraceWarning("	init.json have not Param[sFileType].	");
			bInitNormal = FALSE;
			return;
		}
	}
	fJsonFile.close();
}