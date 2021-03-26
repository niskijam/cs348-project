import mysql.connector
import connection_info


def get_list_sales():
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "SELECT * FROM Sales;"
    sales = []
    try:
        cursor.execute(query)
        for (id, prod_id, cust_id, amnt, loc_id, date) in cursor:
            sales.append({
                "SalesID": id,
                "ProductID": prod_id,
                "CustomerID": cust_id,
                "SaleAmount": amnt,
                "LocationID": loc_id,
                "Date": date
            })

    except Exception as e:
        print("Oi Got Err:")
        print(e)
        cursor.close()
        cnx.close()
        return []

    cursor.close()
    cnx.close()
    return sales