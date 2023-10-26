#include <iostream>
#include <vector>
#include <map>
using namespace std;

// siz -> group별 사이즈
int N, M, X, siz;
// 연결된 등수들
vector<int> adj[100001];
// 연결되지 않은것들 따로 세어주기
vector<pair<int, int>> group;
// 방문 & 깊이
int visited[100001];

int RANK(int u)
{
	siz++;
	// 연결된거 돌면서 깊이 늘려주고 DFS
	for (int v : adj[u])
		if (visited[v] == 0)
		{
			visited[v] = visited[u] + 1;
			RANK(v);
		}

	return siz;
}

int main()
{
	cin >> N >> M >> X; 

	for (int i = 0; i < M; i++)
	{
		int a, b;
		cin >> a >> b;
		// 연결해주기
		adj[a].push_back(b);
	}

	for (int i = 1; i <= N; i++)
	{
		// 방문했으면 패스
		if (visited[i])
			continue;
		// 사이즈 초기화
		siz = 0;
		// 그룹 첫 값의 rank = 1
		visited[i] = 1;
		// DFS
		siz = RANK(i);
		// 그룹넣기
		group.push_back({ i,siz });
	}

	// 최소값
	int min = visited[X];

	// 최대값
	int max = 0;
	if (group.size() > 1)
	{
		for (pair<int, int> p : group)
		{
			if(p.first != X)
				max += p.second;
		}
	}
	max += visited[X];
	
			


	return 0;
}