from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(
    name="Flask-EmailVerifier",
    version="0.1.0",
    url="https://github.com/whois-api-llc/flask-email-verifier",
    license="MIT",
    author="Whois API, Inc.",
    author_email="support@whoisxmlapi.com",
    description="The simplest library for email verification for Flask.",
    long_description=open(normpath(join(dirname(abspath(__file__)), "README.rst"))).read(),
    py_modules=["flask_email_verifier"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=["Flask", "email-verifier"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
