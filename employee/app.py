import mysql.connector

def insert_employee(request):
    print("inside def")
    is_inserted = 0
    try:
        cnx = mysql.connector.connect(user='root', password='marchipoya',
                                  host='127.0.0.1',
                                  database='task')
        curser = cnx.cursor()
        insert_stmt = (
            "INSERT INTO Employee_Details (Employee_Name, Salary, Department)"
            "VALUES (%s, %s, %s)"
        )
        data = (request.employeeName, request.salary, request.department)
        result = curser.execute(insert_stmt, data)

        # result = curser.execute(query)

        cnx.commit()
        is_inserted = 1
    except:
        print("error while inserting the employee")

    finally:
        cnx.close()

    return is_inserted

def delete_employee(request):
    is_deleted = 0
    try:
        cnx = mysql.connector.connect(user='root', password='marchipoya',
                                  host='127.0.0.1',
                                  database='task')
        curser = cnx.cursor()
        delete_stmt = (f"DELETE FROM Employee_Details WHERE id = '{request.id}'")
        # print(delete_stmt)
        # data = (request.id)
        # print(data)
        result = curser.execute(delete_stmt)
        cnx.commit()
        is_deleted = 1
    except:
        print("error while deleting the employee")

    finally:
        cnx.close()

    return is_deleted

def update_employee(request):
    is_updated = 0
    try:
        cnx = mysql.connector.connect(user='root', password='marchipoya',
                                  host='127.0.0.1',
                                  database='task')
        curser = cnx.cursor()
        print("before query")
        update_stmt = (f"UPDATE Employee_Details SET Employee_Name = '{request.employeeName}', Salary = '{request.salary}', Department = '{request.department}' WHERE id = '{request.id}'")
        print(update_stmt)

        # data = (request.employeeName, request.salary, request.department, request.id)
        # print(data)
        result = curser.execute(update_stmt)
        # print(result)

        cnx.commit()
        is_updated = 1
    except:
        print("error while updating the employee")

    finally:
        cnx.close()

    return is_updated

def select_employee(request):
    is_selected = 0
    try:
        cnx = mysql.connector.connect(user='root', password='marchipoya',
                                  host='127.0.0.1',
                                  database='task')
        curser = cnx.cursor()
        select_stmt = (f"select * from Employee_Details WHERE id = '{request.id}'")
        print(select_stmt)

        result = curser.execute(select_stmt)

        cnx.commit()
        is_selected = 1

    except:
        print("error while selecting the employee")

    finally:
        cnx.close()

    return is_selected






