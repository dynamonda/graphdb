// node.h

#ifndef _GRAPHDB_NODE_H_
#define _GRAPHDB_NODE_H_

class Node{
public:
    Node(int id);
    virtual ~Node();

    void info();
    
private:
    int id_;
};

#endif 