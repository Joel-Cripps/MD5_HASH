#md5hash.py
#Returns a list of md5 hash values of the files in a Directory
#Joel Cripps
#May 18th 2014
import hashlib
import os
import sys

from Md5_hash_Compare import dicts

def main():
    topyb = False
    topy_dict = {}
    startdir = raw_input("File directory to start at: ")
    write_to_file = raw_input("Would you like to write output to a file?(y/n)")
    if write_to_file == 'y':
        sys.stdout = open('output.txt','w')

    for startdir, dirnames,filenames in os.walk(startdir):
        for file_ in filenames:
            
            if topyb == False:
                #add to dict file , hash
                #topy.write(md5hash(os.path.join(startdir,file_)))
                topy_dict[os.path.join(startdir, file_)] =  md5hash(os.path.join(startdir,file_))
            else:                
                print file_ , md5hash(os.path.join(startdir,file_))
    
    a = dicts()                
    a.add_dict(topy_dict)
    a.pickload()
    #a = add_dict(topy_dict)
    if write_to_file == 'y':
        sys.stdout.close()
    elif topyb == True:
        print 'yes'
        

    
def md5hash(x):
    try:
        #x = raw_input("File Name")
        file_open = open(x,'rb')   
        y = hashlib.md5()
        while True:
            byte_data = file_open.read(8192)
            if not byte_data:
                break
            y.update(byte_data)
        #print y.hexdigest()
        return y.hexdigest()
    except IOError:
        pass
   #print hashlib.md5(open(x, 'rb').read()).hexdigest()

def topy(x):
    pass
    

main()
