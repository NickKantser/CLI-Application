from click.testing import CliRunner
import unittest
from unittest.mock import patch
import file_client

class TestFileClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()

    # Tests case of invalid command
    @patch('file_client.requests')
    def test_unkown_command(self, mock_req):
        result = self.runner.invoke(file_client.cli, ['unkown_command'])
        self.assertNotEqual(result.exit_code, 0)

    # Tests case of invalid option
    def test_unkown_option(self):
        result = self.runner.invoke(file_client.cli, ['--unkown_option'])
        self.assertNotEqual(result.exit_code, 0)

        result = self.runner.invoke(file_client.cli, ['-unkown_option'])
        self.assertNotEqual(result.exit_code, 0)

    # Tests all default's values of options
    @patch('file_client.requests')
    def test_default_of_options(self, mock_req):
        result = self.runner.invoke(file_client.cli, ['stat', '2'])

        mock_req.get.assert_called_once_with('http://localhost:8000/file/2/stat')
        self.assertEqual(result.exit_code, 0)

    # Tests that http:// is in the address and if not it's added
    @patch('file_client.requests')
    def test_http_in_address(self, mock_req):
        result = self.runner.invoke(file_client.cli, ['--django-server=somelink', 'read', '1'])

        mock_req.get.assert_called_once_with('http://somelink/file/1/read')
        self.assertEqual(result.exit_code, 0)

    # Tests if the request's content of the valid host with valid address is writed to the file
    @patch('file_client.requests')
    def test_valid_host_with_file_output(self, mock_req):
        mock_req.get.return_value.status_code = 200
        mock_req.get.return_value.content = b"{'name': 'some.txt'}"

        with self.runner.isolated_filesystem():
            result = self.runner.invoke(file_client.cli, ['--output=text.txt',
                                                          'stat', '1'])
            with open('text.txt', 'rb') as f:
                file_content = f.read()

        mock_req.get.assert_called_once_with('http://localhost:8000/file/1/stat')
        self.assertEqual(file_content, mock_req.get.return_value.content)
        self.assertEqual(result.exit_code, 0)

    # Tests if the request's content of the valid host with valid address is printed to stdout
    @patch('file_client.requests')
    def test_valid_host_with_standard_output(self, mock_req):
        mock_req.get.return_value.status_code = 200
        mock_req.get.return_value.content = b"{'filename': 'some.txt'}"


        result = self.runner.invoke(file_client.cli, ['stat', '1'])

        mock_req.get.assert_called_once_with('http://localhost:8000/file/1/stat')
        self.assertEqual(result.stdout_bytes, mock_req.get.return_value.content)
        self.assertEqual(result.exit_code, 0)

    # Tests request of the valid host with invalid address -> file output
    @patch('file_client.requests')
    def test_request_error_with_file_output(self, mock_req):
        mock_req.get.return_value.status_code = 404
        status_code = mock_req.get.return_value.status_code
        expected_output = f'Request error!\n{status_code} status code\n'
        expected_output = expected_output.encode()

        with self.runner.isolated_filesystem():
            result = self.runner.invoke(file_client.cli, ['--output=text.txt',
                                                          'stat', '1'])
            with open('text.txt', 'rb') as f:
                file_content = f.read()

        mock_req.get.assert_called_once_with('http://localhost:8000/file/1/stat')
        self.assertEqual(expected_output, file_content)
        self.assertEqual(result.exit_code, 0)

    # Tests request of the valid host with invalid address -> stdout
    @patch('file_client.requests')
    def test_request_error_with_stdout(self, mock_req):
        mock_req.get.return_value.status_code = 404
        status_code = mock_req.get.return_value.status_code
        expected_output = f'Request error!\n{status_code} status code\n'
        expected_output = expected_output.encode()

        result = self.runner.invoke(file_client.cli, ['stat', '1'])

        mock_req.get.assert_called_once_with('http://localhost:8000/file/1/stat')
        self.assertEqual(expected_output, result.stdout_bytes)
        self.assertEqual(result.exit_code, 0)

    # Tests case of invalid address -> file output
    def test_invalid_address_with_file_output(self):
        url = 'http://localhost:8000'
        backend = 'django'

        expected_output = f'Can\'t connect to the {backend} server at address {url}\n'
        expected_output = expected_output.encode()

        with self.runner.isolated_filesystem():
            result = self.runner.invoke(file_client.cli, ['--output=text.txt',
                                                          'stat', '1'])

            with open('text.txt', 'rb') as f:
                file_content = f.read()


        self.assertEqual(expected_output, file_content)
        self.assertEqual(result.exit_code, 0)

    # Tests case of invalid address -> stdout
    def test_invalid_address_with_stdout(self):
        url = 'http://localhost:8000'
        backend = 'django'

        expected_output = f'Can\'t connect to the {backend} server at address {url}\n'
        expected_output = expected_output.encode()

        result = self.runner.invoke(file_client.cli, ['stat', '1'])

        self.assertEqual(expected_output, result.stdout_bytes)
        self.assertEqual(result.exit_code, 0)

    # Test that if --backend=django, then request address corresponds to the --django-server option
    @patch('file_client.requests')
    def test_backend_rest_and_base_url(self, mock_req):
        mock_req.get.return_value.status_code = 200
        mock_req.get.return_value.content = b"{'filename': 'some.txt'}"


        result = self.runner.invoke(file_client.cli, ['--backend=django',
                                                      '--flask-server=http://localhost:14000/',
                                                      '--django-server=http://localhost:15000/',
                                                      'read', '2'])

        mock_req.get.assert_called_once_with('http://localhost:15000/file/2/read')
        self.assertEqual(result.exit_code, 0)

    # Test that if --backend=flask, then request address corresponds to the --flask-server option
    @patch('file_client.requests')
    def test_backend_grpc_and_grpc_server(self, mock_req):
        mock_req.get.return_value.status_code = 200
        mock_req.get.return_value.content = b"{'filename': 'some.txt'}"

        result = self.runner.invoke(file_client.cli, ['--backend=flask',
                                                      '--flask-server=http://localhost:14000/',
                                                      '--django-server=http://localhost:15000/',
                                                      'read', '2'])

        mock_req.get.assert_called_once_with('http://localhost:14000/file/2/read')
        self.assertEqual(result.exit_code, 0)

if __name__ == '__main__':
    unittest.main()
