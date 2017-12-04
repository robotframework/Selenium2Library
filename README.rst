Selenium2Library
================

Selenium2Library is a web testing library for `Robot Framework`_
that uses the Selenium_ tool internally. The project is hosted on
GitHub_ and downloads can be found from PyPI_.

Starting from version 3.0, Selenium2Library is renamed to SeleniumLibrary_
and this project exists mainly to help with transitioning.

Versions
--------

Selenium2Library 3.0 and newer extend the new SeleniumLibrary_ and thus
contain exactly the same code and functionality. There have been lot of
internal changes in the library, but external functionality provided by
keywords should be fully backwards compatible. Libraries and tools using
Selenium2Library internally may need to be updated to support
Selenium2Library 3.0, though. Selenium2Library 1.8 is the latest, and last,
legacy version with the old architecture and code.

Selenium2Library 3.0 supports Python 2.7 as well as Python 3.3 and newer.
Selenium2Library 1.8 supports Python 2.6-2.7.

Keyword documentation
---------------------

- `Selenium2Library 3.0`__ (latest)
- `Selenium2Library 1.8`__ (legacy)

__ http://robotframework.org/Selenium2Library/Selenium2Library.html
__ http://robotframework.org/Selenium2Library/Selenium2Library-1.8.0.html


Installation
------------

The recommended approach to install Selenium2Library, regardless the version,
is using pip_.

Install (or upgrade) the latest Selenium2Library version::

    pip install --upgrade robotframework-selenium2library

Install the legacy Selenium2Library 1.8.0 version::

    pip install robotframework-selenium2library==1.8.0


.. _Robot Framework: http://robotframework.org
.. _Selenium: http://seleniumhq.org
.. _PyPI: https://pypi.python.org/pypi/robotframework-selenium2library
.. _GitHub: https://github.com/robotframework/Selenium2Library
.. _SeleniumLibrary: https://github.com/robotframework/SeleniumLibrary
.. _pip: http://pip-installer.org
