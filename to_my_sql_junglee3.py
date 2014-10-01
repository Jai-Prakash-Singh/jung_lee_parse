import glob
import multiprocessing
import time 
import MySQLdb
import ast
from datetime import datetime


num_fetch_threadsm = 10
enclosure_queuem = multiprocessing.JoinableQueue()

def my_strip(x):
    try:
        x = str(x).strip()
        x = MySQLdb.escape_string(x).strip()
    except:
        x = str(x.encode("ascii", "ignore")).strip()
        x = MySQLdb.escape_string(x).strip()

    return x

        


def main(directory, filename):
    db = MySQLdb.connect("localhost","root","xxxx","jungleesecond")
    cursor = db.cursor()

    f = open(filename)
    
    for line in f:
        try:
            dte = time.strftime("%d:%m:%y")
            line_split = ast.literal_eval(str(line).strip())
            line_split = tuple(map(my_strip, line_split + [dte]))


            sqlentry = """insert into jungleesecond_seller_data ( product_id,  	target_link, seller, selliing_price, dte)
                                               values ("%s", "%s", "%s", "%s", "%s")"""


            sqlentry = sqlentry %(line_split) 
            result = "inserted.................................................................................................................."
        
        

            try:
                cursor.execute(sqlentry)
                db.commit()
                print result

            except:
                try:
                    db.ping()
                    cursor.execute(sqlentry)
                    db.commit()
                    print result
                except:
                    db.rollback()
                    print "rollback. ........................................................................................................"
        
        except:
            pass    
        
    db.close()



def main3(i, q):
    for directory,  filename in iter(q.get, None):
        try:
            main(directory, filename)
        except:
            pass

        time.sleep(2)
        q.task_done()

    q.task_done()



def supermain(directory):
    flptrn = "%s/ct_cl_sct_scl_ssct_sscl_br_bl_pl_info2.txt" %(directory)
    csv_file_list = glob.glob(flptrn)
    

    procs = []

    for i in range(num_fetch_threadsm):
        procs.append(multiprocessing.Process(name = str(i), target=main3, args=(i, enclosure_queuem,)))
        procs[-1].start()

    for filename in csv_file_list:
        enclosure_queuem.put((directory, filename.strip()))

    enclosure_queuem.join()

    for p in procs:
        enclosure_queuem.put(None)

    enclosure_queuem.join()

    for p in procs:
        p.join(1800)    



if __name__=="__main__":
    tstart = datetime.now()
    directory = "/home/desktop/working_sites/junglee/junglee_dir"
    supermain(directory)
    filename = "/home/desktop/working_sites/junglee/junglee_dir/ct_cl_sct_scl_ssct_sscl_br_bl_pl_info2.txt"
    main(directory, filename)
    
    tend = datetime.now()
    print tend - tstart

