#include <iostream>
using namespace std;

int main(){
	int values[5] = {1,8,5,3,6};
	int arrSize = 5;
	int posisi = 1;
	int newValue = 7;
	
	int tempValues[arrSize+1];
	for(int i = 0; i < arrSize; i++){
		tempValues[i] = values[i];
		cout << tempValues[i] << " "; //pembuktian sebelum
	}
	cout << endl;
	
	for(int i = arrSize; i > posisi; i--){
		tempValues[i] = tempValues[i-1];
	}
	tempValues[posisi] = newValue;
	
	for(int i = 0; i <= arrSize; i++){ //pembuktian sesudah
		cout << tempValues[i] << " ";
	}
}
