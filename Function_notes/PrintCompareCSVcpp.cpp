#include<string>
#include<tchar.h>
#include<windows.h>
#include<vector>
#include<sstream>
#include<iostream>
#include<fstream>
//---------------
#include"Common.h"
using namespace std;


void PrintCompareCSV(vector<string>&srcPath, string Version_1, string Version_2)
{
	vector<string>srcCSVs;
	vector<vector<string>>concluCSV;

	for (int i = 0; i < srcPath.size(); i++)
	{
		GetAllCsvFileFromPath(srcPath[i], srcCSVs, Version_1);
	}

	for (int i = 0; i < srcPath.size(); i++)
	{
		GetAllCsvFileFromPath(srcPath[i], srcCSVs, Version_2);
	}

	cout << "Total nums of .csv files: " << srcCSVs.size() << endl;

	ofstream conclusionCSV;
	string conclusionFileName = srcPath[0] + "./conclusion" + Version_1 + "_" + Version_2 + ".csv";
	conclusionCSV.open(conclusionFileName, ios::trunc);

	vector<string>tempStr;

	tempStr.push_back("File Name");
	tempStr.push_back("Total");
	tempStr.push_back("Fail_" + Version_1);
	tempStr.push_back("Fail_" + Version_2);
	tempStr.push_back("FR Diff(%)");
	tempStr.push_back("AVG DUR_" + Version_1);
	tempStr.push_back("AVG DUR_" + Version_2);
	tempStr.push_back("DUR Diff(%)");

	concluCSV.push_back(tempStr);

	for (int i = 0; i < srcCSVs.size() / 2; i++)
	{
		int irealIndx = i;
		int icsvLength = srcCSVs.size() / 2;
		ifstream tempFile1(srcCSVs[irealIndx], ios::in);
		ifstream tempFile2(srcCSVs[irealIndx + icsvLength], ios::in);
		size_t startPos = srcCSVs[irealIndx].find_last_of('\\');
		string fileName = srcCSVs[irealIndx].substr(startPos + 1);
		vector<string> strTemp;

		vector<vector<string>>singleCSV1;
		string lineStr1;

		while (getline(tempFile1, lineStr1))
		{
			stringstream ssTemp(lineStr1);
			string strTemp;
			vector<string>lineAry;

			while (getline(ssTemp, strTemp, ','))
				lineAry.push_back(strTemp);
			singleCSV1.push_back(lineAry);

		}
		tempFile1.close();

		vector<vector<string>> singleCSV2;
		string lineStr2;
		while (getline(tempFile2, lineStr2))
		{
			stringstream ssTemp(lineStr1);
			string strTemp;
			vector<string>lineAry;
			while (getline(ssTemp, strTemp, ','))
				lineAry.push_back(strTemp);
			singleCSV2.push_back(lineAry);
		}
		tempFile2.close();

		int startIndx = singleCSV1.size() - 7;

		if (startIndx <= 0 || singleCSV1.size() != singleCSV2.size())
		{
			continue;
		}
		else
		{
			double duration1 = 0;
			double duration2 = 0;
			int totalNum = 0;
			int failNum1 = 0;
			int failNum2 = 0;
			double failureRateDiff = 0;
			double durationDiff = 0;

			stringstream sstmp;
			sstmp << singleCSV1[startIndx][1];
			sstmp >> totalNum;
			sstmp.clear();
			sstmp.str("");//sstmp.str("");
			sstmp << singleCSV1[startIndx + 2][1];
			sstmp >> failNum1;
			sstmp.clear();
			sstmp.str("");
			sstmp << singleCSV2[startIndx + 2][1];
			sstmp >> failNum2;
			sstmp.clear();
			sstmp.str("");
			sstmp << singleCSV1[startIndx + 4][1];
			sstmp >> duration1;
			sstmp.clear();
			sstmp.str("");
			sstmp << singleCSV2[startIndx + 4][1];
			sstmp >> duration2;
			sstmp.clear();
			sstmp.str("");

			failureRateDiff = (double)((failNum2 - failNum1) / (double)totalNum) * 100;
			durationDiff = (double)((duration2 - duration1) / duration1) * 100;

			strTemp.push_back(fileName);
			strTemp.push_back(singleCSV1[startIndx][1]);
			strTemp.push_back(singleCSV1[startIndx + 2][1]);
			strTemp.push_back(singleCSV2[startIndx + 2][1]);
			sstmp << failureRateDiff;
			strTemp.push_back(sstmp.str());
			sstmp.clear();
			sstmp.str("");
			strTemp.push_back(singleCSV1[startIndx + 4][1]);
			strTemp.push_back(singleCSV2[startIndx + 4][1]);
			sstmp << durationDiff;
			strTemp.push_back(sstmp.str());
			sstmp.clear();
			sstmp.str("");

			concluCSV.push_back(strTemp);

		}
	}

	for (int j = 0; j < concluCSV.size(); j++)
	{
		for (int m = 0; m < concluCSV[j].size(); m++)
		{
			if (m != concluCSV[j].size() - 1)
			{
				conclusionCSV << concluCSV[j][m] << ",";
			}
			else
			{
				conclusionCSV << concluCSV[j][m] << endl;
			}
		}
	}
	conclusionCSV.close();
}