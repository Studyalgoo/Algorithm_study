#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

// 노드생성
struct Node 
{
	int y, x, ret;
	char cal;
};

int N; 
char _map[6][6];
int moveY[2] = { 0, 1 };
int moveX[2] = { 1, 0 };
vector<int> v;
queue<Node> q;

// 계산을 위한 함수
int Calcul(int a, int b, char cal)
{
	if (cal == '+')
		return a + b;
	else if (cal == '-')
		return a - b;
	else if (cal == '*')
		return a * b;
}

void BFS()
{
	// 아스키코드 48 -> 0
	q.push({ 1, 1, _map[1][1] - 48});

	while (q.size())
	{
		int y = q.front().y;
		int x = q.front().x;
		int ret = q.front().ret;
		char cal = q.front().cal;
		q.pop();

		// 목표지점 도착시 값 vector에 넣기
		if (y == N && x == N)
		{
			v.push_back(ret);
			continue;
		}

		// 오른쪽, 아래 움직이기
		for (int i = 0; i < 2; i++)
		{
			int nextY = y + moveY[i];
			int nextX = x + moveX[i];

			// 범위 체크
			if (nextY > N || nextX > N)
				continue;

			// cal 값이 없으면 _map값은 연산자
			if (cal == '\0')
				q.push({ nextY, nextX, ret, _map[nextY][nextX]});
			// cal 값 있으면 _map값은 숫자
			else
				q.push({ nextY, nextX, Calcul(ret, _map[nextY][nextX] - 48, cal), '\0' });
		}
	}
}


int main()
{
	// 입출력 시간
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	// 입력
	cin >> N;
	for (int y = 1; y <= N; y++)
		for (int x = 1; x <= N; x++)
			cin >> _map[y][x];

	// bfs
	BFS();

	// 최대값
	int mx = *max_element(v.begin(), v.end());
	// 최소값
	int mn = *min_element(v.begin(), v.end());

	// 출력
	cout << mx << " " << mn;

	return 0;
}