import mysql.connector as connector
class Database:
    #Creating constractor
    def __init__(self):
        self.con=connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='mk55',
                                    database='dbmsproject')
        
        self.con.autocommit=True
        self.cur=self.con.cursor(dictionary=True)

        def create_me_reg():
            query="""create table if not exists me_reg(
                        stu_roll int not NULL primary key, 
                        stu_name varchar(255) not NULL,
                        semester int not NULL,
                        gender enum('M','F'),
                        dob Date,
                        phone varchar(12),
                        stu_email varchar(255) not NULL,
                        stu_addrs varchar(500)
                        );
                        """
            self.cur.execute(query)

        def create_ee_reg():
            query="""create table if not exists ee_reg(
                        stu_roll int not NULL primary key, 
                        stu_name varchar(255) not NULL,
                        semester int not NULL,
                        gender enum('M','F'),
                        dob Date,
                        phone varchar(12),
                        stu_email varchar(255) not NULL,
                        stu_addrs varchar(500)
                        );
                        """
            self.cur.execute(query)

        def create_cse_reg():
            query="""create table if not exists cse_reg(
                        stu_roll int not NULL primary key, 
                        stu_name varchar(255) not NULL,
                        semester int not NULL,
                        gender enum('M','F'),
                        dob Date,
                        phone varchar(12),
                        stu_email varchar(255) not NULL,
                        stu_addrs varchar(500)
                        );
                        """
            self.cur.execute(query)


        def create_civil_reg():
            query="""create table if not exists civil_reg(
                        stu_roll int not NULL primary key, 
                        stu_name varchar(255) not NULL,
                        semester int not NULL,
                        gender enum('M','F'),
                        dob Date,
                        phone varchar(12),
                        stu_email varchar(255) not NULL,
                        stu_addrs varchar(500)
                        );
                        """
            self.cur.execute(query)

        def create_mtech_reg():
            query="""create table if not exists mtech_reg(
                        stu_roll int not NULL primary key, 
                        stu_name varchar(255) not NULL,
                        semester int not NULL,
                        gender enum('M','F'),
                        dob Date,
                        phone varchar(12),
                        stu_email varchar(255) not NULL,
                        stu_addrs varchar(500)
                        );
                        """
            self.cur.execute(query)

        def create_mca_reg():
            query="""create table if not exists mca_reg(
                        stu_roll int not NULL primary key, 
                        stu_name varchar(255) not NULL,
                        semester int not NULL,
                        gender enum('M','F'),
                        dob Date,
                        phone varchar(12),
                        stu_email varchar(255) not NULL,
                        stu_addrs varchar(500)
                        );
                        """
            self.cur.execute(query)


        def create_ece_reg():
            query="""create table if not exists ece_reg(
                        stu_roll int not NULL primary key, 
                        stu_name varchar(255) not NULL,
                        semester int not NULL,
                        gender enum('M','F'),
                        dob Date,
                        phone varchar(12),
                        stu_email varchar(255) not NULL,
                        stu_addrs varchar(500)
                        );
                        """
            self.cur.execute(query)

        def create_chem_reg():
            query="""create table if not exists chem_reg(
                        stu_roll int not NULL primary key, 
                        stu_name varchar(255) not NULL,
                        semester int not NULL,
                        gender enum('M','F'),
                        dob Date,
                        phone varchar(12),
                        stu_email varchar(255) not NULL,
                        stu_addrs varchar(500)
                        );
                        """
            self.cur.execute(query)

        try:
            create_me_reg()
            print("Created")
            create_ee_reg()
            print("Created")
            create_cse_reg()
            print("Created")
            create_civil_reg()
            print("Created")
            create_mtech_reg()
            print("Created") 
            create_mca_reg()
            print("Created")
            create_ece_reg()
            print("Created")
            create_chem_reg()
            print("Created")                                            
        except exception as e:
            print(e)


    # insert student
    def insert_me_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
       query="""insert into me_reg(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
            values({},'{}',{},'{}','{}','{}','{}','{}')""".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
       print(query)
    #    cur=self.cnx.cursor()    #curser method is come from connection
       self.cur.execute(query)
    #    self.cnx.commit()    #commit method come from connection

    # update-student
    def update_me_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
        query="update me_reg set stu_roll={}, stu_name='{}', semester={}, gender='{}', dob='{}', phone='{}', stu_email='{}', stu_addrs='{}' where stu_roll={}".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs, stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)


        # Delete student
    def delete_me_reg(self, stu_roll):
        query="delete from me_reg where stu_roll={}".format(stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)  

       # fetch all
    def fetch_all_me_reg(self):
        query="select * from me_reg"
        self.cur.execute(query)
        result=self.cur.fetchall()
        # cur=self.cnx.cursor()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return 0

     #fetch one
    def fetch_one_me_reg(self, stu_roll):
        query="select * from me_reg where stu_roll={}".format(stu_roll)
        self.cur.execute(query)
        result=self.cur.fetchall()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return {"message":"No data Found"}   



    # insert student
    def insert_ee_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
       query="""insert into ee_reg(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
            values({},'{}',{},'{}','{}','{}','{}','{}')""".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
       print(query)
    #    cur=self.cnx.cursor()    #curser method is come from connection
       self.cur.execute(query)
    #    self.cnx.commit()    #commit method come from connection

    # update-student
    def update_ee_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
        query="update ee_reg set stu_roll={}, stu_name='{}', semester={}, gender='{}', dob='{}', phone='{}', stu_email='{}', stu_addrs='{}' where stu_roll={}".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs, stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)


        # Delete student
    def delete_ee_reg(self, stu_roll):
        query="delete from ee_reg where stu_roll={}".format(stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)  

       # fetch all
    def fetch_all_ee_reg(self):
        query="select * from ee_reg"
        self.cur.execute(query)
        result=self.cur.fetchall()
        # cur=self.cnx.cursor()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return 0

     #fetch one
    def fetch_one_ee_reg(self, stu_roll):
        query="select * from ee_reg where stu_roll={}".format(stu_roll)
        self.cur.execute(query)
        result=self.cur.fetchall()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return {"message":"No data Found"} 



    # insert student
    def insert_cse_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
       query="""insert into cse_reg(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
            values({},'{}',{},'{}','{}','{}','{}','{}')""".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
       print(query)
    #    cur=self.cnx.cursor()    #curser method is come from connection
       self.cur.execute(query)
    #    self.cnx.commit()    #commit method come from connection

    # update-student
    def update_cse_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
    #    self.cnx.commit()    #commit method come from connection
        query="update cse_reg set stu_roll={}, stu_name='{}', semester={}, gender='{}', dob='{}', phone='{}', stu_email='{}', stu_addrs='{}' where stu_roll={}".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs, stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)


        # Delete student
    def delete_cse_reg(self, stu_roll):
        query="delete from cse_reg where stu_roll={}".format(stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)  

       # fetch all
    def fetch_all_cse_reg(self):
        query="select * from cse_reg"
        self.cur.execute(query)
        result=self.cur.fetchall()
        # cur=self.cnx.cursor()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return 0
     #fetch one
    def fetch_one_cse_reg(self, stu_roll):
        query="select * from cse_reg where stu_roll={}".format(stu_roll)
        self.cur.execute(query)
        result=self.cur.fetchall()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return {"message":"No data Found"} 


    # insert student
    def insert_civil_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
       query="""insert into civil_reg(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
            values({},'{}',{},'{}','{}','{}','{}','{}')""".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
       print(query)
    #    cur=self.cnx.cursor()    #curser method is come from connection
       self.cur.execute(query)
    #    self.cnx.commit()    #commit method come from connection

    # update-student
    def update_civil_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
    #    self.cnx.commit()    #commit method come from connection
        query="update civil_reg set stu_roll={}, stu_name='{}', semester={}, gender='{}', dob='{}', phone='{}', stu_email='{}', stu_addrs='{}' where stu_roll={}".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs, stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)


        # Delete student
    def delete_civil_reg(self, stu_roll):
        query="delete from civil_reg where stu_roll={}".format(stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)  

       # fetch all
    def fetch_all_civil_reg(self):
        query="select * from civil_reg"
        self.cur.execute(query)
        result=self.cur.fetchall()
        # cur=self.cnx.cursor()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return 0

     #fetch one
    def fetch_one_civil_reg(self, stu_roll):
        query="select * from civil_reg where stu_roll={}".format(stu_roll)
        self.cur.execute(query)
        result=self.cur.fetchall()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return {"message":"No data Found"}   


    # insert student
    def insert_mtech_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
       query="""insert into mtech_reg(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
            values({},'{}',{},'{}','{}','{}','{}','{}')""".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
       print(query)
    #    cur=self.cnx.cursor()    #curser method is come from connection
       self.cur.execute(query)
    #    self.cnx.commit()    #commit method come from connection

    # update-student
    def update_mtech_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
    #    self.cnx.commit()    #commit method come from connection
        query="update mtech_reg set stu_roll={}, stu_name='{}', semester={}, gender='{}', dob='{}', phone='{}', stu_email='{}', stu_addrs='{}' where stu_roll={}".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs, stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)


        # Delete student
    def delete_mtech_reg(self, stu_roll):
        query="delete from mtech_reg where stu_roll={}".format(stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)  

       # fetch all
    def fetch_all_mtech_reg(self):
        query="select * from mtech_reg"
        self.cur.execute(query)
        result=self.cur.fetchall()
        # cur=self.cnx.cursor()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return 0

     #fetch one
    def fetch_one_mtech_reg(self, stu_roll):
        query="select * from mtech_reg where stu_roll={}".format(stu_roll)
        self.cur.execute(query)
        result=self.cur.fetchall()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return {"message":"No data Found"}

    # insert student
    def insert_mca_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
       query="""insert into mca_reg(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
            values({},'{}',{},'{}','{}','{}','{}','{}')""".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
       print(query)
    #    cur=self.cnx.cursor()    #curser method is come from connection
       self.cur.execute(query)
    #    self.cnx.commit()    #commit method come from connection

    # update-student
    def update_mca_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
    #    self.cnx.commit()    #commit method come from connection
        query="update mca_reg set stu_roll={}, stu_name='{}', semester={}, gender='{}', dob='{}', phone='{}', stu_email='{}', stu_addrs='{}' where stu_roll={}".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs, stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)


        # Delete student
    def delete_mca_reg(self, stu_roll):
        query="delete from mca_reg where stu_roll={}".format(stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)  

       # fetch all
    def fetch_all_mca_reg(self):
        query="select * from mca_reg"
        self.cur.execute(query)
        result=self.cur.fetchall()
        # cur=self.cnx.cursor()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return 0

     #fetch one
    def fetch_one_mca_reg(self, stu_roll):
        query="select * from mca_reg where stu_roll={}".format(stu_roll)
        self.cur.execute(query)
        result=self.cur.fetchall()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return {"message":"No data Found"}


    # insert student
    def insert_ece_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
       query="""insert into ece_reg(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
            values({},'{}',{},'{}','{}','{}','{}','{}')""".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
       print(query)
    #    cur=self.cnx.cursor()    #curser method is come from connection
       self.cur.execute(query)
    #    self.cnx.commit()    #commit method come from connection

    # update-student
    def update_ece_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
    #    self.cnx.commit()    #commit method come from connection
        query="update ece_reg set stu_roll={}, stu_name='{}', semester={}, gender='{}', dob='{}', phone='{}', stu_email='{}', stu_addrs='{}' where stu_roll={}".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs, stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)


        # Delete student
    def delete_ece_reg(self, stu_roll):
        query="delete from ece_reg where stu_roll={}".format(stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)  

       # fetch all
    def fetch_all_ece_reg(self):
        query="select * from ece_reg"
        self.cur.execute(query)
        result=self.cur.fetchall()
        # cur=self.cnx.cursor()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return 0

     #fetch one
    def fetch_one_ece_reg(self, stu_roll):
        query="select * from ece_reg where stu_roll={}".format(stu_roll)
        self.cur.execute(query)
        result=self.cur.fetchall()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return {"message":"No data Found"}


    # insert student
    def insert_chem_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
       query="""insert into chem_reg(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
            values({},'{}',{},'{}','{}','{}','{}','{}')""".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs)
       print(query)
    #    cur=self.cnx.cursor()    #curser method is come from connection
       self.cur.execute(query)
    #    self.cnx.commit()    #commit method come from connection

    # update-student
    def update_chem_reg(self, stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs):
    #    self.cnx.commit()    #commit method come from connection
        query="update chem_reg set stu_roll={}, stu_name='{}', semester={}, gender='{}', dob='{}', phone='{}', stu_email='{}', stu_addrs='{}' where stu_roll={}".format(stu_roll, stu_name, semester, gender, dob, phone ,stu_email, stu_addrs, stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)


        # Delete student
    def delete_chem_reg(self, stu_roll):
        query="delete from chem_reg where stu_roll={}".format(stu_roll)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)  

       # fetch all
    def fetch_all_chem_reg(self):
        query="select * from chem_reg"
        self.cur.execute(query)
        result=self.cur.fetchall()
        # cur=self.cnx.cursor()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return 0

     #fetch one
    def fetch_one_chem_reg(self, stu_roll):
        query="select * from chem_reg where stu_roll={}".format(stu_roll)
        self.cur.execute(query)
        result=self.cur.fetchall()
        if len(result)>0:
            # return json.dumps(result)
            return result
        else:
            return {"message":"No data Found"}

    