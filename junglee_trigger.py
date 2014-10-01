import sys 
import shutil 
import time

def main():
    sys.path.append("/home/desktop/working_sites/junglee")
    directory = "/home/desktop/working_sites/junglee/junglee_dir"


    directory2 = "%s%s" %(directory, time.strftime("%d%m%y"))
    #import code1_first_junglee
    #code1_first_junglee.supermain(directory)

    #import mysql_con_python_junglee
    #mysql_con_python_junglee.supermain()

    #import mysql_con_python_junglee2
    #mysql_con_python_junglee2.supermain()

    #import to_my_sql_junglee
    #to_my_sql_junglee.supermain(directory)

    #import mysql_con_python_junglee3
    #mysql_con_python_junglee3.supermain()

    #import to_my_sql_junglee3
    #to_my_sql_junglee3.supermain(directory)

    import upload_to_cdn
    upload_to_cdn.supermain(directory)

    shutil.move(directory, directory2)    

    


if __name__=="__main__":
    main()
