#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int N, S, T;
priority_queue<int, vector<int>, greater<int>> pq;
vector<pair<int, int>> v;

int main()
{
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> S >> T;
		v.push_back(make_pair(S, T));
	}

	sort(v.begin(), v.end());

	for (pair<int, int> p : v)
	{
		pq.push(p.second);

		if (p.first >= pq.top())
			pq.pop();
	}
	
	cout << pq.size();

	return 0;
}
