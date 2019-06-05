# Node Backup Utility

## About

This is a utility which allows for backuping up of a lightning node

## Usage

### Configuring

You need to have a config file in ```$HOME/.lncm/nodebackup.toml```

```
provider = "dropbox"
nodename = "testnode"
logfile = "/var/log/backup.log"
backupfile = "/root/.lnd/data/chain/bitcoin/mainnet/channel.backup"
pidfile = "/var/run/nodebackup.pid"

[apikeys]
dropbox = "APIKEYHERE"

```

### Installing

```bash
sudo /usr/bin/python3 -m pip install inotify
sudo /usr/bin/python3 -m pip install lndnodebackup
```

### Running

After installing the utility simply invoke

```bash
lndnodebackup
```

This will run as a background task, which you can kill based on the PID.

## Building

```bash
sudo python3 -m pip install setuptools wheel twine
python3 setup.py bdist_wheel
sudo pip3 install dist/nodebackup-X.X.X-py3-none-any.whl
```

### Distributing

```bash
python3 setup.py sdist bdist_wheel
# Test
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# production
python3 -m twine upload dist/* 
```

## Todo / What's Missing

- [ ] Support for Amazon S3
- [ ] Connect to LND and backup each channel individually and grab the text backup as well
- [ ] Robustness (maybe have the script handle SIGHUP to reload configuration file)
