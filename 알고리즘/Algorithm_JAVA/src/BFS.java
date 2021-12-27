import java.util.Iterator;
import java.util.LinkedList;

public class BFS {
    // 인접 리스트 사용하여 구현
    private int V;
    private LinkedList<Integer> bfs[];

    BFS(int v) {
        V = v;
        bfs = new LinkedList[v];

        for(int i = 0; i < v; ++i) {
            bfs[i] = new LinkedList();
        }
    }

    // 노드를 연결 v -> w
    void addEdge(int v, int w) {
        bfs[v].add(w);
    }

    // s부터 시작
    void bfs(int s) {
        // 노드의 방문 여부 판단
        boolean visited[] = new boolean[V];
        LinkedList<Integer> queue = new LinkedList<Integer>();

        visited[s] = true;
        queue.add(s);

        while(queue.size() != 0) {
            // 방문한 노드를 큐에서 반환
            s = queue.poll(); // 가장 첫 번째 요소를 반환한 후 삭제

            // 방문한 노드와 인접한 모든 노드를 가져온다.
            Iterator<Integer> i = bfs[s].listIterator();
            while(i.hasNext()) {
                int n = i.next();

                // 방문 x 노드면 방문한 것으로 표시하고 큐에 추가
                if(!visited[n]) {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }
}

// 코드 참고: https://gmlwjd9405.github.io/2018/08/15/algorithm-bfs.html