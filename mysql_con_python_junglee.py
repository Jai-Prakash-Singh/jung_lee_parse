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
    

    sql = """create table IF NOT EXISTS  jungleesecond_data (
               task_id int(11) NOT NULL AUTO_INCREMENT,
               product_id varchar(100),
	       product_title text,
               product_title_zovon text, 
	       target_link varchar(300),
	       selliing_price text,
	       category varchar(300), 
               sub_category varchar(300), 
               ss_cate varchar(300), 
               ss_link varchar(300), 
	       brand text, 
	       image_link varchar(300), 
               sort_image_link varchar(300), 
	       mrp text, 
	       color text, 
	       target varchar(300), 
	       product_url varchar(500), 
	       seller text, 
	       meta_title text, 
	       meta_desc text, 
	       size text, 
	       product_desc  text,
	       product_spec text,
	       dte text,
	       status varchar(10),
               primary key (task_id)
	    )"""

    cursor.execute(sql)

    try:
        sql2 = "create unique index jungleesecond_index on jungleesecond_data (product_url)"
        cursor.execute(sql2)
        db.commit()   
    except:
        pass

    try:
        sql2 = "create  index jungleesecond_index2 on jungleesecond_data (product_id,target_link, category, sub_category,ss_cate, ss_link,\
            image_link, sort_image_link, target, status  )"
        cursor.execute(sql2)
        db.commit()
    except:
        pass



    sql = """alter ignore  table  jungleesecond_data add upload_status enum('NO','YES', 'F') DEFAULT 'NO';"""

    try:
        cursor.execute(sql)
        db.commit()
    except:
        pass

    

    sql = """UPDATE  jungleesecond_data  set upload_status = 'NO' """
    cursor.execute(sql)
    db.commit()


    sql = """alter ignore  table  jungleesecond_data add upload_image_status enum('NO','YES', 'F') DEFAULT 'NO';"""

    try:
        cursor.execute(sql)
        db.commit()
    except:
        pass


    sql = """alter ignore  table  jungleesecond_data add upload_to_imgtable  enum('NO','YES', 'F') DEFAULT 'NO';"""

    try:
        cursor.execute(sql)
        db.commit()
    except:
        pass


    sql = """alter ignore  table   jungleesecond_data  add index  jungleesecond_data_index2  (upload_status, upload_image_status, upload_to_imgtable)"""
    try:
        cursor.execute(sql)
        db.commit()
    except:
        pass


    sql = """alter ignore  table  jungleesecond_data  add failing_status  enum('NO','YES', 'F') DEFAULT 'NO';"""

    try:
        cursor.execute(sql)
        db.commit()
    except:
        pass


    sql = """alter ignore  table  jungleesecond_data  add  seller_brand varchar (100) DEFAULT "www.junglee.com" """

    try:
        cursor.execute(sql)
        db.commit()
    except:
        pass

    sql = """ALTER TABLE jungleesecond_data  CHANGE ss_cate ss_category varchar(300) """
    try:
        cursor.execute(sql)
        db.commit()
    except:
        pass




    sql = """create table IF NOT EXISTS  jungleesecond_new_images (
               task_id int(11) NOT NULL AUTO_INCREMENT,
               product_id varchar(50),
               image_link varchar(300), 
               primary key (task_id)
             )"""

    cursor.execute(sql)


    sql = """alter ignore  table  jungleesecond_new_images add upload_image_status enum('NO','YES', 'F') DEFAULT 'NO';"""

    try:
        cursor.execute(sql)
        db.commit()
    except:
        pass

    

    sql = """alter ignore  table jungleesecond_new_images add failing_status  enum('NO','YES', 'F') DEFAULT 'NO';"""
    
    try:
        cursor.execute(sql)
        db.commit()
    except:
        pass

    sql = """alter ignore  table   jungleesecond_new_images  add index jungleesecond_new_images_index  (upload_image_status, 
               failing_status, product_id, image_link)"""
    try:
        cursor.execute(sql)
        db.commit()
    except:
        pass




  
    db.close()
    print " db_close()......................................................"



    



if __name__=="__main__":
    supermain()

