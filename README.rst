.. image:: https://img.shields.io/badge/License-MIT-green.svg
    :alt: subdomains-lookup-py license
    :target: https://opensource.org/licenses/MIT

.. image:: https://img.shields.io/pypi/v/subdomains-lookup.svg
    :alt: subdomains-lookup-py release
    :target: https://pypi.org/project/subdomains-lookup

.. image:: https://github.com/whois-api-llc/subdomains-lookup-py/workflows/Build/badge.svg
    :alt: subdomains-lookup-py build
    :target: https://github.com/whois-api-llc/subdomains-lookup-py/actions

========
Overview
========

The client library for
`Subdomains Lookup API <https://subdomains.whoisxmlapi.com/>`_
in Python language.

The minimum Python version is 3.6.

Installation
============

.. code-block:: shell

    pip install subdomains-lookup

Examples
========

Full API documentation available `here <https://subdomains.whoisxmlapi.com/api/documentation/making-requests>`_

Create a new client
-------------------

.. code-block:: python

    from subdomainslookup import *

    client = Client('Your API key')

Make basic requests
-------------------

.. code-block:: python

    # Get categories for a domain name.
    response = client.get('google.com')
    for record in response.result.records:
        print("Domain: " + record.domain)

Advanced usage
-------------------

Extra request parameters

.. code-block:: python

    # Get records count
    print(response.result.count)

    # Get raw API response in XML
    xml_response = client.get_raw('google.com', output_format=Client.XML_FORMAT)


Response model overview

.. code-block:: python

    Response:
        - search: str
        - result: Result
            - count: int
            - records: [Record]
                - domain: str
                - first_seen: datetime.datetime
                - last_seen: datetime.datetime
