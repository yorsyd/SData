#include <iostream>
using namespace std;

void insertArray(int values[], int newValue, int posisi, int arrSize) {
    cout << "sebelum: ";
    for (int i = 0; i < arrSize ; i++) {
        cout << values[i] << " ";
    }
    cout << endl;
    
    int tempArray[arrSize + 1];
    for (int i = 0; i < posisi; i++) {
        tempArray[i] = values[i];
	}
    
    tempArray[posisi] = newValue;
    for (int i = posisi + 1; i < arrSize + 1; i++) {
        tempArray[i] = values[i - 1];
    }

    cout << "after: ";
    for (int i = 0; i < arrSize + 1; i++) {
        cout << tempArray[i] << " ";
    }
}

int main() {
    int values[] = {3, 7, 2, 9};
    int arrSize = sizeof(values) / sizeof(values[0]);
    int newValue = 11;
    int posisi = 2;

    insertArray(values, newValue, posisi, arrSize);

    return 0;
}
