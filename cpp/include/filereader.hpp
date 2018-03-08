// filereader.hpp

#ifndef _GRAPHDB_FILEREADER_H_
#define _GRAPHDB_FILEREADER_H_

#include <string>
#include <memory>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/json_parser.hpp>

class FileReader{
public:
    virtual ~FileReader(){};
};

class JsonFileReader : public FileReader{
public:
    JsonFileReader(){};
    JsonFileReader(const std::string &filepath){
        boost::property_tree::ptree pt;
        boost::property_tree::read_json(filepath, pt);
    }
};

#endif