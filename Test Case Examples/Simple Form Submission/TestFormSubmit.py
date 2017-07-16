import unittest
import numbers
import string


# Test Object
class TestForm():
    def __init__(self):
        self.text_field_value = ''
        self.text_field_exists = False
        self.text_field_type = 'text'
        self.button_text = 'Submit'
        self.button_type = 'input'
        self.button_exists = False

    # Sets page elements values to True
    def page_load(self):
        try:
            self.button_exists = True
            self.text_field_exists = True
        except Exception as ex:
            return ex

    # Returns value submitted
    def submit(self, value=None):
        try:
            self.text_field_value = value
            return self.text_field_value
        except Exception as ex:
            return ex


class UserSubmission(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(UserSubmission,self).__init__(*args, **kwargs)
        self.my_form = my_form = TestForm()
        self.my_form.page_load() # changes elements exists properties to true

    def test_single_digit(self):
        value = self.my_form.submit(5)
        self.assertTrue((value > 9), 'Value was less than 2 digits.')

    def test_is_double_digit(self):
        value = self.my_form.submit(33)
        self.assertTrue((9 < value < 100), 'Value is not a double digit.')

    def test_triple_digit(self):
        value = self.my_form.submit(121)
        self.assertTrue(value < 100, 'Value was more than 2 digits.')

    def test_if_none(self):
        value = self.my_form.submit()
        self.assertIsNotNone(value, 'Value supplied is None.') #

    def test_is_not_zero(self):
        value = self.my_form.submit(0)
        self.assertTrue((value != 0), 'Value is equal to zero.')

    def test_negative_number(self):
        value = self.my_form.submit(-1)
        self.assertGreater(value, 0 ,'Value is a negative number.')

    def test_if_float(self):
        value = self.my_form.submit(10.0)
        self.assertFalse(isinstance(value,float),'Value is not an integer type.')

    def test_if_long(self):
        value = self.my_form.submit(10000)
        self.assertFalse(isinstance(value,numbers.Integral), 'Value is not an integer type.')

    def test_is_int(self):
        value = self.my_form.submit(10)
        self.assertTrue(isinstance(value,int), msg='') # verify is an integer

    def test_if_alpha(self):
        value = self.my_form.submit('a')
        self.assertFalse(value.isalpha(),'Value is non-numeric type.')

    def test_if_alpha_num(self):
        value = self.my_form.submit('a1')
        self.assertFalse(value.isalpha(),'Value is an alpaha-numeric type.')

    def test_if_special_char(self):
        value = self.my_form.submit('$%')  # Filter for special character submissions
        self.assertFalse(any(v in value for v in string.punctuation), 'Value supplied was special-character.')

    def test_button_text(self):
        self.assertTrue((self.my_form.button_text == 'Submit'), 'The button text is incorrect.')

    def test_button_exists(self):
        self.assertTrue((self.my_form.button_exists is True), 'Submit button did not load successfully.')

    def test_button_type(self):
        self.assertTrue((self.my_form.button_type == 'text'), 'Incorrect button type.')

    def test_text_field_exists(self):
        self.assertTrue(self.my_form.text_field_exists is True, 'Text field did not load successfully.')

    def test_field_type(self):
        self.assertTrue((self.my_form.text_field_type == 'text'),'Incorrect field type.')

    def test_page_load_successful(self):
        self.assertTrue((self.my_form.button_exists is True and self.my_form.text_field_exists is True),
                        'Page did not load successfully.')

    def test_page_load_exception(self):
        self.assertRaises(BaseException, self.my_form.page_load())  # Validates exception is thrown

    def test_submit_button_exception(self):
        self.assertRaises(BaseException, self.my_form.submit())  # Validates exception is thrown



if __name__ == '__main__':
    unittest.main()