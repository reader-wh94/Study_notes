import java.util.Iterator;
import java.util.LinkedList;

public class DFS {
    //인접 리스트 & 재귀 사용
    private int V;
    private LinkedList<Integer> dfs[];

    DFS(int v) {
        V = v;
        dfs = new LinkedList[v];

        // 인접 리스트 초기화
        for(int i = 0; i < v; ++i) {
            dfs[i] = new LinkedList();
        }
    }

    void addEdge(int v, int w) {
        dfs[v].add(w);
    }

    void dfs(int v) {
        boolean visited[] = new boolean[v];

        // v를 시작 노드로 재귀 호출
        DFSUtil(v, visited);
    }

    void DFSUtil(int v, boolean visited[]) {
        // 현재 노드를 방문한 것으로 변경
        visited[v] = true;
        System.out.println(v + " ");

        // 방문한 노드와 인접한 모든 노드를 가져온다.
        Iterator<Integer> it = dfs[v].listIterator();
        while(it.hasNext()) {
            int n = it.next();
            // 방문하지 않은 노드면 해당 노드를 시작 노드로 변경
            if(!visited[n]) {
                DFSUtil(n, visited);
            }
        }
    }
}

// 코드 참조: https://devuna.tistory.com/32
