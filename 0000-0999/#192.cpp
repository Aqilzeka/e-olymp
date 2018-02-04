#include <iostream>
#include <cmath>
using namespace std;
 
int main() {
	int n;
	cin >> n;
	int a, b, c, d, k;
	a = 1;
	b = 1;
	c = 2;
	bool x;
	int counter = 0;
	while (counter < n){
		x = true;
		c = a + b;
		a = b;
		b = c;
		for (int j = 2; j <= sqrt(c) && x; j++) {
			if((c%j) == 0){
				x = false;
			}
		}
		if (x){
			counter ++;
		}
	}
	cout << c;
	return 0;
}
