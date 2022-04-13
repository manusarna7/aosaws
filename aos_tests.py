import unittest
import aos_methods as methods


class AOSPositiveTestCases(unittest.TestCase):

    @staticmethod  # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_create_new_account():  # test_ in the name is mandatory
        methods.setup()
        methods.validate_homepage_texts_links()
        methods.create_new_account()
        methods.validate_new_account()
        methods.log_out()
        methods.log_in()
        methods.validate_new_account()
        methods.checkout_shoppingcart()
        methods.validate_order()
        methods.log_out()
        methods.log_in()
        methods.validate_order_page()
        methods.delete_order_page()
        methods.log_in()
        methods.delete_user_account()
        methods.log_in()
        methods.teardown()
