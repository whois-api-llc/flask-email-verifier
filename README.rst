Flask-EmailVerifier
===================

The easiest way to verify emails in your Flask application.


Meta
----
- Author: Whois API, Inc.
- Email: support@whoisxmlapi.com
- Site: https://emailverification.whoisxmlapi.com


Prerequisites
-------------

To use this library, you'll need to create a free Email Verification API
account: https://emailverification.whoisxmlapi.com/

If you haven't done this yet, please do so now.


Installation
------------

To install ``Flask-EmailVerifier`` using `pypi <https://pypi.org/>`_, simply run:

.. code-block:: console

    $ pip install Flask-EmailVerifier

In the root of your project directory.


Usage
-----

Once you have `Flask-EmailVerifier` installed, you can use it to easily
verify an email address.

This library gives you access to the Email Verification API that
you can use in your application in any number of ways.

Here's a simple Flask app that makes use of the email address verification
and returns an email address information:

.. code-block:: python

    from flask import Flask, make_response
    from flask_email_verifier import EmailVerifier
    from json import dumps, loads

    app = Flask(__name__)
    # Initialize the extension
    verifier = EmailVerifier(app)

    @app.route('/email/<email>')
    def email(email):
        # Retrieve an info for the given email address
        email_address_info = verifier.verify(email)
        if email_address_info is not None:
            data = dumps(loads(email_address_info.json_string), indent=4)
            resp = make_response(data, 200)
            resp.headers['Content-Type'] = 'application/json'
        else:
            resp = make_response('None', 404)
        return resp

Don't forget to specify your API key:

.. code-block:: bash

    $ export EMAIL_VERIFIER_KEY='your-key'


Here's the sort of data you might get back when performing a email
verification request:

.. code-block:: json

    {
        "emailAddress": "test.email@gmail.com",
        "formatCheck": "true",
        "smtpCheck": "false",
        "dnsCheck": "true",
        "freeCheck": "true",
        "disposableCheck": "false",
        "catchAllCheck": "false",
        "mxRecords": [
            "alt3.gmail-smtp-in.l.google.com",
            "alt1.gmail-smtp-in.l.google.com",
            "alt2.gmail-smtp-in.l.google.com",
            "alt4.gmail-smtp-in.l.google.com",
            "gmail-smtp-in.l.google.com"
        ],
        "audit": {
            "auditCreatedDate": "2018-11-14 13:05:09.000 UTC",
            "auditUpdatedDate": "2018-11-14 13:05:09.000 UTC"
        }
    }


In the event an email verification request can't finish successfully, the data
returned will be `None`. This library will *never* throw an exception.
This decision was made strategically: if you cannot verify user's email, it
doesn't mean that this user is bad.
