from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_register_a_new_participant_info(self):
        # Gaurav gets new entries on Symposium Participants.
        # Gaurav fires his browser to fill each participant in the
        # Mahati Portal
        self.browser.get('http://localhost:8000')

        # Gaurav notices the title of the browser, 'Mahati'
        self.assertIn('Mahati', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
