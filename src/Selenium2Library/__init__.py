# Copyright 2008-2011 Nokia Networks
# Copyright 2011-2016 Ryan Tomac, Ed Manlove and contributors
# Copyright 2016-     Robot Framework Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from SeleniumLibrary import SeleniumLibrary


__version__ = '3.0.0a2'


class Selenium2Library(SeleniumLibrary):

    def get_keyword_documentation(self, name):
        if name == '__intro__':
            doc = SeleniumLibrary.__doc__
            doc = doc.replace('SeleniumLibrary', 'Selenium2Library')
            return """\
| Starting from 3.0.0a1 release Selenium2Library project has moved to SeleniumLibrary project. Currently the Selenium2Library is only a wrapper to the SeleniumLibrary.
| More details can be found from the Selenium2Library project: https://github.com/robotframework/Selenium2Library and from SeleniumLibrary project: https://github.com/robotframework/SeleniumLibrary
""" + doc
        else:
            doc = SeleniumLibrary.get_keyword_documentation(self, name)
            return doc.replace('SeleniumLibrary', 'Selenium2Library')
