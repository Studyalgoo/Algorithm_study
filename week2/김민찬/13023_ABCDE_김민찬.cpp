#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N, M;
vector<int> adj[2000];
bool visited[2000];

bool DFS(int now, int depth)
{
	// 깊이가 5일때 -> 친구 관계O
	if (depth == 5)
		return true;

	// 친구관계에 값이 있는것만
	for (int next : adj[now])
	{
		// 이미 방문한 곳이면 패스
		if (visited[next])
			continue;

		// 방문했다고 체크
		visited[next] = true;

		// 다시 dfs
		if (DFS(next, depth + 1))
			return true;

		// 같은 깊이 부분 체크 해주기 위해 false로 만들기
		visited[next] = false;
	}

	return false;
}

int main()
{
	cin >> N >> M;

	for (int i = 0; i < M; i++)
	{
		int a, b;
		cin >> a >> b;

		// 양방향 그래프로 만들어 주기
		adj[a].push_back(b);
		adj[b].push_back(a);
	}

	for (int i = 0; i < N; i++)
	{
		// visited 초기화
		fill_n(visited, 2000, false);
		
		// 내가 들어갈 곳 방문 체크해주기
		visited[i] = true;

		// 깊이가 4인곳이 존재하면
		if (DFS(i, 1))
		{
			// 1 출력
			cout << 1;
			return 0;
		}
	}

	// 없으면 2출력
	cout << 0;

	return 0;
}