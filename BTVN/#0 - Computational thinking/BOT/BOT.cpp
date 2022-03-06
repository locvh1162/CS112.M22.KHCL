#include <iostream>
using namespace std;

int main()
{
	int n, sum;
	cin >> n;
	int a[100];
	for (int i = 0; i < n; i++)
		cin >> a[i];
	int lai = 0, p = 0, q = 0;
	for (int i = 0; i < n; i++) {
		sum = 0;
		sum += a[i];
		for (int j = i; j < n; j++) {
			if (i != j) sum += a[j];
			if (sum > lai) {
				lai = sum;
				p = i + 1;
				q = j + 1;
			}
		}
	}
	cout << p << " " << q << " " << lai << endl;
	return 0;
}
