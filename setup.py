from setuptools import setup, find_packages

setup(
    name='file-client',
    version='1.0.0',
    description='Simple CLI application which retrieves and prints data from the backend',
    py_modules=['file_client'],
    install_requires=[
        'Flask==2.0.1',
        'click==8.0.3',
        'SQLAlchemy==1.4.36',
        'requests==2.27.1',
        'psycopg2-binary==2.9.3'
    ],
    entry_points={
        'console_scripts': [
            'file-client=file_client.file_client:cli'
        ],
    },
)
