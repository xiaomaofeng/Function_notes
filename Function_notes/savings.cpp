#include<iostream>
#include"savings.h"
using namespace std;
Savings* Savings::pFirst = 0;
int Savings::count = 0;

Savings::Savings(unsigned accNo, float balan)
{
	acntNumber = accNo;
	balance = balan;
	count++;
	if (pFirst == 0)
	{
		pFirst = this;
	}
	else
	{
		Savings* pS = pFirst;
		for (pS->pNext; pS = pS->pNext;);
		pS->pNext = this;
	}
	pNext = 0;
}

unsigned Savings::AccountNo()
{
	return acntNumber;
}

//float Savings::AcntBalan()
//{
//	return acntBalance;
//}

Savings* Savings::First()
{
	return pFirst;
}

Savings* Savings::Next()
{
	return pNext;
}

int Savings::NoAccounts()
{
	return count;
}

void Savings::Display()
{
	cout << "Savings account number:" << acntNumber
		<< "=" << balance << endl;
}

void Savings::Deposit(float amount)
{
	balance += amount;
}

void Savings::Withdrawal(float amount)
{
	if (balance < amount)
	{
		cout << "Insufficient funds:balance" << balance
			<< ",withdrawal" << amount << endl;
	}
	else
	{
		balance -= amount;
	}
}