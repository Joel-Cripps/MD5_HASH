#Dicts of the previous md5 file hashes
#var name is the name of the root directory
import datetime
from get_dict_num import *
import dict_storage
import pickle
import pprint

class dicts(object):
    
    def __init__(self):
        #self.temp = get_dict_num.get_dict_num()
        self.dictnum = 0
        self.date = datetime.datetime.now()

    def getDictNum(self):
        return self.dictnum

    def add_dict_num(self):
        self.dictnum = self.dictnum + 1

    def add_dict(self,dict_):
        pickle.dump(dict_,open("Save.pkl","a+b"))
        
    def toString(self,dict_):
        return "self.dict" + str(self.temp) + "=" + str(dict_)
    
    def pickleobj(self):
        pass
    
    def pickload(self):
        open_file = open("Save.pkl",'rb')
        pprint.pprint(pickle.load(open_file))
        
    
    
