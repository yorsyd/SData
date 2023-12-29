#include <iostream>
using namespace  std;

//fungsi
int faktorial(int n){
	if (n == 0){
		return 1;
	}
	return (faktorial(n-1)*n);
}

//prosedur
void faktorial1(int n){
	int hasil = 1;
	for (int i = 1; i <= n; i++){
		hasil = hasil*i;
	}
	cout << hasil;
}

int main(){
//	cout << faktorial(3);
	
	faktorial1(5);	
}

