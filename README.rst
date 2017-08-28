Selenium2library for Robot Framework
====================================

Selenium2Library is a web testing library for `Robot Framework`_
that leverages the `Selenium 2`_  (WebDriver) libraries from the
`Selenium`_ project.


Selenium2Library project has been moved to `SeleniumLibrary`_ from release
3.0.0 Alpha 2 onwards.

The latest `Selenium2Library 1.8.0 release keyword documentation`_ is available
from Selenium2Library project.

Selenium versions
-----------------

There are three main version of Selenium: `Selenium Remote Control`_ (RC or Selenium
1), `Selenium 2`_ and `Selenium 3`_.

The Selenium RC works only with major browsers that has JavaScript enabled. It
also requires a selenium server which automatically launches and kill browsers.
The Selenium RC is not anymore maintained by the Selenium.

The Selenium 2 supports Selenium RC and Selenium WebDirver. Selenium WebDriver
does not need separate server to launch and kill servers and it has simpler
and more concise API then Selenium RC.

The Selenium 3 supports only Selenium WebDirver and has started to adopt
the `W3C WebDriver`_. If excluding the dropped Selenium RC support, Selenium 3
is a drop in replacement for Selenium 2.

Selenium support in Robot Framework
-----------------------------------

The SeleniumLibrary version up to 2.9.2 supports only the Selenium RC.

The Selenium2Library versions up to 1.8.0 and from SeleniumLibrary 3.0.0
version onwards supports Selenium 2 and 3

Python support
--------------

The SeleniumLibrary version up to 2.9.2 and the Selenium2Library
versions up to 1.8.0 supports only Python 2

Starting from SeleniumLibrary 3.0.0 version onwards Python 2 and Python 3.3+ are
supported.

History
-------

The SeleniumLibrary up to 2.9.2 version was actively developed by using the
Selenium RC. When the Selenium 2 reached mature enough state, the Selenium2Library
was forked from SeleniumLibary and modified to use the Selenium WebDriver. The
SeleniumLibrary, with Selenium RC support, active development ended
when Selenium RC was deprecated.

When Selenium 3 was released it was adopted by the Selenium2Library
because Selenium 3 is a drop in replacement for Selenium 2. Also the
Selenium2Library relies only on the WebDriver technology and it did not
need any changes to support Selenium 3.

In release 3.0.0, it was decided to rename the Selenium2Library back to
SeleniumLibrary. This was done because the name more resembles what the library
supports and enables.

.. _Robot Framework: http://robotframework.org
.. _Selenium 2: http://www.seleniumhq.org/projects/webdriver/
.. _Selenium 3: http://www.seleniumhq.org/projects/webdriver/
.. _Selenium: http://selenium.openqa.org
.. _SeleniumLibrary: https://github.com/robotframework/SeleniumLibrary
.. _Selenium2Library 1.8.0 release keyword documentation: http://robotframework.org/Selenium2Library/Selenium2Library.html
.. _Selenium Remote Control: http://www.seleniumhq.org/projects/remote-control/
.. _W3C WebDriver: https://www.w3.org/TR/webdriver/