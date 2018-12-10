#include<stdio.h>
#include<iostream>
#include<queue>
using namespace std;

struct BinaryTree
{
	int val;
	BinaryTree* left;
	BinaryTree* right;
	BinaryTree(int data)
		:val(data), left(nullptr), right(nullptr) {

	}

};

void PrintTree(BinaryTree* arr[])
{
	queue<BinaryTree*>rel;
	rel.push(arr[0]);
	while (!rel.empty())
	{
		BinaryTree* front = rel.front();

		cout << front->val;
		rel.pop();
		if (front->left != nullptr)
			rel.push(front->left);
		if (front->right != nullptr)
			rel.push(front->right);
	}
	
}

int main()
{
	BinaryTree* arr[6];
	arr[0] = new BinaryTree(0);
	arr[1] = new BinaryTree(1);
	arr[2] = new BinaryTree(2);
	arr[3] = new BinaryTree(3);
	arr[4] = new BinaryTree(4);
	arr[5] = new BinaryTree(5);
	arr[0]->left = arr[1];
	arr[0] -> right = arr[2];
	arr[1]->left = arr[3];
	arr[3]->left = arr[5];
	arr[2]->right = arr[4];
	PrintTree(arr);
	for (int i = 0; i < 6; i++)
		delete arr[i];
	return 0;

}