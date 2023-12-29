#include <iostream>
using namespace std;

void insertArray(int arr[], int newValue, int position, int arrSize){
	int resultValues[arrSize+1];
	
	cout << "Sebelum: ";
	for(int i = 0; i < arrSize; i++){
		resultValues[i] = arr[i];
		cout << resultValues[i] << " ";
	} cout << endl;
	
	for(int i = arrSize; i > position; i--){
		resultValues[i] = resultValues[i-1];
	}
	resultValues[position] = newValue;
	
	cout << "Sesudah: ";
	for(int i = 0; i <= arrSize; i++){
		cout << resultValues[i] << " ";
	}
}

int main(){
	int values[] = {3,7,2,9};
	int posisi = 2;
	int newValue = 11;
	int arrSize = sizeof(values)/sizeof(values[0]);
	
	insertArray(values, newValue, posisi, arrSize);
}
