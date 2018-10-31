// Function_notes.cpp: 定义控制台应用程序的入口点。
//



#include<iostream>
#include<vector>
using namespace std;

void FinancialManagement(vector<double>&money, double &average)
{
	double sum = 0;
	for (int i = 0; i < money.size(); i++)
	{
		sum += money[i];
	}
	average = sum / 12;
	cout << "$" << average << endl;
}

int main()
{
	vector<double>money;
	double average = 0;
	double temp;
	for (int j = 0; j < 12; j++)
	{
		cin >> temp;
		money.push_back(temp);
	}
	FinancialManagement(money, average);
	//system("pause");
	return 0;

}

