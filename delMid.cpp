#include <iostream>
using namespace std;

int main(){
	int values[5] = {1,8,11,3,6};
	int arrSize = 5;
	int posisi = 1;
	
	for(int i = 0; i < arrSize; i++){ //pembuktian sebelum
		cout << values[i] << ", ";
	} cout << endl;
	
	for(int i = posisi; i < arrSize-1; i++){
		values[i] = values[i+1];
	}
	
	values[arrSize-1];
	
	for(int i = 0; i < arrSize-1; i++){ //pembuktian sesudah
		cout << values[i] << ", ";
	}
}
