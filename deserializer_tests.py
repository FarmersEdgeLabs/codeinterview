from deserializer import Order


def main():
    # Testing the generated object for attributes:
    test = '{"order_id":19384,"customerid":165,"cost":76.40,"dateordered":"02-09-2020","datecompleted":"04-10-2020"}'
    test_order = Order(test)
    assert test_order.order_id == 19384
    assert test_order.customer_id == 165
    assert test_order.cost == 76.40
    assert test_order.date_ordered == '02-09-2020'
    assert test_order.date_completed == '04-10-2020'
    print('Deserializer tests passed!')


if __name__ == '__main__':
    main()
