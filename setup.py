'''
   Copyright 2019 nolim1t.co

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

from setuptools import setup

setup(
    name="lndnodebackup",
    version="0.0.2",
    packages=["nodebackup"],
    install_requires=["toml", "dropbox", "docopt"],
    entry_points={"console_scripts": ["lndnodebackup = nodebackup.nodebackup:main"]},

    zip_safe=True,
    author="nolim1t",
    author_email="hello@nolim1t.co",
    description="bitcoin lightning node (LND) backup daemon service",
    license="Apache 2.0",
    keywords="bitcoin lightning node backup",
    url="https://gitlab.com/nolim1t/nodebackup"
 )
