# Graph DataBase

グラフ理論によるデータベースを構築することを目標にしたプロジェクト

## データベースの構成

データベースはGraphオブジェクトで表される

基本的にデータベースは以下の要素からなる
1. Node
2. Edge

### Graph

- name      : std::string
- node_list : map< std::string, Node >
- edge_list : map< std::string, Edge >
- node_next_index   : int
- edge_next_index   : int

Node, Edgeのリストは連想配列が推奨される。
要素の削除でインデックスがずれることを防ぐためである。

### Node

ノードは以下の要素を持つ
- id    : int
    - 0から始まる一意のインデックス
- name  : std::string
- info  : dict
    - 任意のデータ格納場所

### Edge

エッジは以下の要素を持つ
- id            : int
    - 0から始まる一意のインデックス
- name          : std::string
- source_node   : Node
- target_node   : Node
- info          : dict
    - 任意のデータ格納場所
