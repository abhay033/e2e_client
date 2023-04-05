from setuptools import setup, find_packages

setup(
    name='e2e_client',
    version='1.1.0',
    description="This a E2E Client tool for Certbot Plugin",
    author="Abhay Bhati",
    author_email="abhaybhati987@gmail.com",
    packages=find_packages(),
    install_requires=['requests', 'setuptools'],
    package_data={
        '': ['*.1'],
        '': ['docs/*.1'],
        'docs': ['*.1'],
    },
 
    include_package_data = True,
)
