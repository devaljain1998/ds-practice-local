#include <vector>
#include <queue>
#include <iostream>
#include <unordered_map>
#include "taskScheduler.h"
using namespace std;

typedef pair<char, int> TaskFreq;


class Compare {
    public:
    // A0 B0 A3 B3 A6 B6
    bool operator()(const TaskFreq a, const TaskFreq b) {
        if (a.second != b.second) return a.second > b.second;
        return a.first > b.first;
    }
};

void print_pq(std::priority_queue<TaskFreq, std::vector<TaskFreq>, Compare> pq)
{
    while (!pq.empty())
    {
        cout << pq.top().first << ", " << pq.top().second << endl;
        pq.pop();
    }
}


int main()
{
    vector<char> tasks{'A', 'A', 'A', 'B', 'B', 'B'};
    int n = 2;
    cpuCycles(tasks, n); cout << endl;

    vector<char> tasks2{'A','C','A','B','D','B'};
    int n2 = 1;
    cpuCycles(tasks2, n2); cout << endl;

    vector<char> tasks3{'A','A','A','B','B','B'};
    int n3 = 3;
    cpuCycles(tasks3, n3); cout << endl;

    return 0;
}
void cpuCycles(vector<char> &tasks, int n)
{
    unordered_map<char, int> taskFreq;
    for (const char &task : tasks)
        ++taskFreq[task];

    priority_queue<TaskFreq, vector<TaskFreq>, Compare> pq;
    for (const auto &[task, freq] : taskFreq)
    {
        for (int i = 0; i < freq; ++i)
        {
            const int order = i * (n + 1);
            pq.push({task, order});
        }
    }

    // print_pq(pq);
    // cout << "size of pq: " << pq.size() << endl;

    vector<char> cpuCycles;
    int currentOrder = 0;
    int ptr = 0;
    while (!pq.empty())
    {
        while (ptr < currentOrder)
        {
            cpuCycles.push_back('I');
            ptr++;
        }

        // append all the tasks in the current order:
        while (!pq.empty() && pq.top().second == currentOrder)
        {
            TaskFreq currentTask = pq.top();
            const char task = currentTask.first;
            const int order = currentTask.second;

            cpuCycles.push_back(task);
            pq.pop();
            ptr++;
        }

        // Update the current Order to the next order:
        if (!pq.empty())
            currentOrder = pq.top().second;
    }

    cout << "CPU cycles: " << cpuCycles.size() << endl;
    for (const char &task : cpuCycles)
        cout << task << " ";
    cout << endl;
}