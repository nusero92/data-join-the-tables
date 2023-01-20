# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''

    query="""SELECT orders.OrderID ,Customers.ContactName, employees.FirstName
FROM Orders
JOIN Customers on orders.CustomerID =customers.CustomerID
JOIN Employees on orders.EmployeeID  =employees.EmployeeID
ORDER BY OrderID"""
    db.execute(query)
    results = db.fetchall()
    return results

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''

    query=""" SELECT Customers.ContactName,  SUM(UnitPrice*Quantity)
FROM OrderDetails
join Orders on orderDetails.OrderID =orders.OrderID
join Customers on orders.CustomerID =customers.CustomerID
group by orders.OrderID
order by Customers.ContactName """
    db.execute(query)
    results = db.fetchall()
    return results

def best_employee(db):
    '''Implement the best_employee method to determine who’s the best employee! By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like: ('FirstName', 'LastName', 6000 (the sum of all purchase)). The order of the information is irrelevant'''
    query=""" """
    db.execute(query)
    results = db.fetchall()
    return results

def orders_per_customer(db):
    '''Return a list of tuples where each tuple contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    query=""" """
    db.execute(query)
    results = db.fetchall()
    return results
