#include <iostream>
using namespace std;

typedef long long ll;

ll A, B, C;

// 모듈로 연산
ll Mod(ll a, ll b)
{
	// 기저사례
	if (b == 1)
		return a % C;

	// b를 반으로 나눈 Mod
	ll ret = Mod(a, b / 2);

	// 나눈 값을 곱해서 % C로 나머지 해준다
	ret = (ret * ret) % C;

	// 홀수일때 a 한번 더 곱해주기
	if (b % 2 == 1)
		ret = (a * ret) % C;

	return ret;
}

int main()
{
	cin >> A >> B >> C;

	cout << Mod(A, B);

	return 0;
}