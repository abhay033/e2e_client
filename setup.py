from setuptools import setup, find_packages

setup(
    name='e2e_client',
    version='0.9.8',
    description="This a E2E Client tool for Certbot Plugin",
    author="Abhay Bhati",
    author_email="abhaybhati987@gmail.com",
    packages=find_packages(),
    install_requires=['requests', 'setuptools'],

    include_package_data = True,
)
