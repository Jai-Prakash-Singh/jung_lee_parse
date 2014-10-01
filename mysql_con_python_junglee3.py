#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb



def supermain():
    db = MySQLdb.connect("localhost","root","xxxx")
    cursor = db.cursor()

    sql = "create database if not exists  jungleesecond"
    cursor.execute(sql)

    sql = "use jungleesecond"
    cursor.execute(sql)
    

    sql = """create table IF NOT EXISTS  jungleesecond_seller_data (
               task_id int(11) NOT NULL AUTO_INCREMENT,
               product_id varchar(100),
	       target_link text,
               seller text, 
	       selliing_price text,
               dte text,
               primary key (task_id)
	    )"""

    cursor.execute(sql)

    db.commit()

  
    db.close()
    print " db_close()......................................................"



    



if __name__=="__main__":
    supermain()

