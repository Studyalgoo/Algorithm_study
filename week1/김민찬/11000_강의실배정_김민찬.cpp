#include <iostream>
#include <algorithm>
using namespace std;

int N, cnt;
bool room[200000];
pair<int, int> p[200000];

void GetClassRoom(int now)
{
	if (room[now])
		return;

	// 방문한 방 체크
	room[now] = true;

	for (int i = now + 1; i < N; i++)
	{
		// 이미 방문한 방이라면 패스
		if (room[i])
			continue;

		// 수업 마치는 시간과 시작하는 시간이 같거나 시작하는 시간이 뒤에 있을 경우
		if (p[now].second <= p[i].first)
		{
			GetClassRoom(i);
			break;
		}
	}
}

int main()
{
	cin >> N;

	int S, T;

	for (int i = 0; i < N; i++)
	{
		cin >> S >> T;
		p[i] = make_pair(S, T);
	}

	// 시간 순서로 정렬
	sort(p, p + N);

	// 방 개수
	cnt = 0;
	for (int i = 0; i < N; i++)
	{
		// 방문한 방이 아닐 경우에만 cnt +1
		if (room[i] == false)
			cnt++;
		GetClassRoom(i);
	}

	cout << cnt;

	return 0;
}