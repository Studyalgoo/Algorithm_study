#include <iostream>
#include <string>
using namespace std;

int N1, N2, T;
string str, str1, str2;

int main()
{
	cin >> N1 >> N2;
	cin >> str1;
	cin >> str2;
	cin >> T;

	// 첫번째 개미 뒤집기
	reverse(str1.begin(), str1.end());

	str = str1 + str2;

	// 시간만큼 for문
	for (int i = 0; i < T; i++)
		// 개미들 방향 체크하기
		for (int j = 0; j < str.size() - 1; j++)
			// j번째 개미가 첫번쨰 그룹에 있는게 맞고 j+1 번째 개미가 두번쨰 그룹에 있는게 맞다면
			if (string::npos != str1.find(str[j]) && string::npos != str2.find(str[j + 1]))
			{
				// 스왑 해주기
				swap(str[j], str[j + 1]);
				// 한칸만 건너뛰면 계속 방향 바뀌기 때문에 2칸 건너뛰기 위해서
				j++;
			}

	cout << str;

	return 0;
}