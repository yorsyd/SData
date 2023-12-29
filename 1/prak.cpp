#include <iostream>
using namespace std;

int delArray(int arr[], int newValue, int position, int arrSize){
	int tempArr[arrSize];
	
	cout << "Sebeluum: ";
	for(int i = 0; i < arrSize; i++){
		tempArr[i] = arr[i];
		cout << arr[i] << " ";
	}
	cout << endl;
	
	arr[arrSize-1];
	for(int i = position; i < arrSize-1; i++){
		arr[i] = tempArr[i+1];
	} 
	
	cout << "Sesudah: ";
	for(int i = 0; i < arrSize-1; i++){
		cout << arr[i] << " ";
	}
}

int main(){
	int values[] = {6, 3, 9, 11, 2};
	int posisi = 2;
	int newValue = 5;
	int arrSize = sizeof(values)/sizeof(values[0]);
	
	delArray(values, newValue, posisi, arrSize);
}
