// edge.h

#ifndef _GRAPHDB_EDGE_H_
#define _GRAPHDB_EDGE_H_

#include "node.h"

class Edge{
public:
    Edge();
    virtual ~Edge();

private:
    Node *source_node_;
    Node *target_node_;
};

#endif