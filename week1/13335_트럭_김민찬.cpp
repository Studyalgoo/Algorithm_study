#include <iostream>
#include <ctime>
using namespace std;

int n, w, L;
int a[1001];
int bridge[101];
int cnt;

void CrossTheBridge()
{
	int now = 0;

	while (true)
	{
		// 트럭 한칸씩 이동
		for (int i = 1; i <= w; i++)
		{
			bridge[i - 1] = bridge[i];
		}

		// 다리 처음 건너는 곳에 now 번째 트럭 넣기
		if (now >= n)
			bridge[w] = 0;
		else
			bridge[w] = a[now];

		// 트럭 무게 총 무게
		int sum = 0;
		for (int i = 1; i <= w; i++)
		{
			sum += bridge[i];
		}

		// 트럭 무게랑 다리 하중 비교
		if (sum > L)
			bridge[w] = 0;
		else
			now++;

		cnt++;

		if (sum == 0)
			break;
	}
}

int main()
{
	// 입력부 시간 줄이기
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> w >> L;
	for (int i = 0; i < n; i++)
		cin >> a[i];

	CrossTheBridge();

	cout << cnt;

	return 0;
}
