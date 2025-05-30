/**
 * @param {number[][]} edges1
 * @param {number[][]} edges2
 * @param {number} k
 * @return {number[]}
 */
var maxTargetNodes = function(edges1, edges2, k) {
    const n = edges1.length + 1;
    const m = edges2.length + 1;
    const buildAdj = (edges, size) => {
        const adj = Array.from({ length : size }, () => []);
        for (const [u, v] of edges){
            adj[u].push(v);
            adj[v].push(u);
        }
        return adj;
    };
    const adj1 = buildAdj(edges1, n);
    const adj2 = buildAdj(edges2, m);

    const DFS = (node, parent, maxLen, adj) => {
        if (maxLen < 0){
            return 0;
        }
        let count = 1; 
        for (const nei of adj[node]){
            if (nei != parent){
                count += DFS(nei, node, maxLen - 1, adj);
            }
        }
        return count;
    };
    let maxCnt2 = 0;
    for (let i = 0; i < m; i++){
        maxCnt2 = Math.max(maxCnt2, DFS(i, -1, k - 1, adj2));
    }
    const res = [];
    for (let i = 0; i < n; i++){
        const cnt1 = DFS(i, -1, k,adj1);
        res.push(cnt1 + maxCnt2);
    }
    return res;

};