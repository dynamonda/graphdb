# Graph DataBase

グラフ理論によるデータベースを構築することを目標にしたプロジェクト

## データベースの構成

データベースはGraphオブジェクトで表される

基本的にデータベースは以下の要素からなる
1. Node
2. Edge

### Graph

- name      : std::string
- node_list : array<Node>
- edge_list : array<Edge>

### Node

ノードは以下の要素を持つ
- id    : int
- name  : std::string
- etc.. : <anytype>

### Edge

エッジは以下の要素を持つ
- id            : int
- name          : std::string
- source_node   : Node
- target_node   : Node
- etc..         : <anytype>
