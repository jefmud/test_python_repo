import os

def file_picker(thisdir = '.'):
    files = os.listdir(thisdir)
    i = 0
    for f in files:
        print i, ':', f
        i += 1
    print 'type in number of file to choose, hitting ENTER for None:'
    fidx = raw_input()
    try:
        return files[int(fidx)]
    except:
        return None
 
def process_file(filename, data={}):
    fh = open(filename,'r')
    while True:
        line = fh.readline().strip()
        if not line:
            break
        line = line.split('\t')
        if line[0] in data:
            val = data[line[0]]
            val.append(int(line[1]))
            data[line[0]] = val
        else:
            data[line[0]] = [int(line[1])]
    return data

def save_dictionary_csv(filename,data):
    fh = open(filename,'w')
    for key, value in data.iteritems():
        line = []
        line.append(key)
        for v in value:
            line.append(v)
        buf = ''
        for item in line:
            buf += str(item) + ','
        fh.write(buf + '\n')
    fh.close()
        
if __name__ == '__main__':
    print "Aggregate multiple TSV files into CSV"
    filename = 'temp'
    data = {}
    while filename:
        filename = file_picker()
        print "You chose %s" % filename
        if filename:
            data = process_file(filename, data)
            print data
    
    print "Enter name of desired CSV file Hit ENTER to cancel:"
    fname = raw_input()
    
    if fname:
        save_dictionary_csv(fname,data)
    print "Done."