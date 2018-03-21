from configparser import ConfigParser
from flask import Flask, render_template, json, request
#from flaskext.mysql import MySQL
 
 
def read_db_config(filename='config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.optionxform=str #make it case sensitive; Transforms the option name option as found in an input file
    parser.read(filename)
 
    # get section, default to mysql
    db = {} # dictionary
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
            #print(item[1])

    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
 
    #print(db)
    return db

if __name__ == '__main__':
    read_db_config()
# read_db_config()