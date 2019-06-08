build:
	/usr/bin/python3 setup.py bdist_wheel

clean:
	/bin/rm -fr ./build/
	/bin/rm -fr ./dist/
	/bin/rm -fr ./lndnodebackup.egg-info/
	/bin/rm -fr ./nodebackup/*.pyc
	/bin/rm -fr ./nodebackup/__pycache__

all:
	/bin/rm -fr ./build/
	/bin/rm -fr ./dist/
	/bin/rm -fr ./lndnodebackup.egg-info/
	/bin/rm -fr ./nodebackup/*.pyc
	/bin/rm -fr ./nodebackup/__pycache__
	/usr/bin/python3 setup.py bdist_wheel

install:
	/usr/bin/pip3 install dist/lndnodebackup-0.0.2rc3-py3-none-any.whl

uninstall:
	/usr/bin/pip3 uninstall lndnodebackup