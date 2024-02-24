import sqlite3 as sql


class Database():
    def __init__(self):
        self.connection = sql.connect('become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        request = 'SELECT sqlite_version();'
        self.cursor.execute(request)
        respond = self.cursor.fetchall()
        print(respond)

    def get_all_users(self):
        request = 'SELECT name, address, city FROM customers;'
        self.cursor.execute(request)
        respond = self.cursor.fetchall()
        print(respond)

    def get_user_address_by_name(self, name):
        request = f'SELECT address, city, postalCode, country FROM customers WHERE name = "{
            name}";'
        self.cursor.execute(request)
        respond = self.cursor.fetchall()
        return respond

    def update_product_qnt_by_id(self, product_id, qnt):
        request = f'UPDATE products SET quantity = {
            qnt} WHERE id = {product_id};'
        self.cursor.execute(request)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        request = f'SELECT quantity FROM products WHERE id = {
            product_id};'
        self.cursor.execute(request)
        respond = self.cursor.fetchall()
        return respond

    def insert_product(self, product_id, name, description, qnt):
        request = f'INSERT OR REPLACE INTO products(id, name, description, quantity) VALUES({
            product_id}, "{name}", "{description}", {qnt});'
        self.cursor.execute(request)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        request = f'DELETE FROM products WHERE id = {product_id};'
        self.cursor.execute(request)
        self.connection.commit()

    def get_detailed_orders(self):
        request = 'SELECT orders.id, customers.name, products.name, products.description, orders.order_date FROM orders JOIN customers ON orders.id = customers.id JOIN products ON orders.id = products.id;'
        self.cursor.execute(request)
        respond = self.cursor.fetchall()
        return respond
