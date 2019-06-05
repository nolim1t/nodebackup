from setuptools import setup

setup(
    name="nodebackup",
    version="0.0.1",
    packages=["nodebackup"],
    install_requires=["toml", "dropbox"],
    entry_points={"console_scripts": ["nodebackup = nodebackup.nodebackup:main"]},

    zip_safe=True,
    author="nolim1t",
    author_email="hello@nolim1t.co",
    description="bitcoin lightning node (LND) backup tool",
    license="Apache 2.0",
    keywords="bitcoin lightning node backup",
    url="https://gitlab.com/nolim1t/nodebackup",

)
