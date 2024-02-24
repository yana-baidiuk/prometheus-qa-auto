import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    database = Database()
    database.test_connection()


@pytest.mark.database
def test_check_all_users():
    database = Database()
    database.get_all_users()


@pytest.mark.database
def test_check_all_users():
    database = Database()
    user = database.get_user_address_by_name('Sergii')
    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    database = Database()
    database.update_product_qnt_by_id(1, 25)
    quantity = database.select_product_qnt_by_id(1)
    assert quantity[0][0] == 25


@pytest.mark.database
def insert_product():
    database = Database()
    database.insert_product(4, 'печиво', 'солодке', 30)
    quantity = database.select_product_qnt_by_id(4)
    assert quantity[0][0] == 30


@pytest.mark.database
def test_product_delete():
    database = Database()
    database.insert_product(99, 'тестові', 'дані', 999)
    database.delete_product_by_id(99)
    quantity = database.select_product_qnt_by_id(99)
    assert len(quantity) == 0


@pytest.mark.database
def test_detailed_orders():
    database = Database()
    orders = database.get_detailed_orders()
    print(orders)
    assert len(orders) == 1
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'
