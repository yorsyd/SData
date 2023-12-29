#include <iostream>
using namespace std;

int* deleteArray(int values[], int arrSize, int posisi) {
    for (int i = posisi; i < arrSize - 1; i++) {
        values[i] = values[i + 1];
    }

    int tempArray[arrSize - 1];
    for (int i = 0; i < arrSize - 1; i++) {
        tempArray[i] = values[i];
    }

    return tempArray;
}

int main() {
    int values[] = {3, 7, 2, 9};
    int arrSize = sizeof(values) / sizeof(values[0]);
    int posisi = 2;

	cout << "Sebelum: ";
    for (int i = 0; i < arrSize; i++) {
        cout << values[i] << " ";
    }
    cout << endl;
    
    int* result = deleteArray(values, arrSize, posisi);
    
    cout << "Sesudah: ";
    for (int i = 0; i < arrSize - 1; i++) {
        cout << values[i] << " ";
    }
}

