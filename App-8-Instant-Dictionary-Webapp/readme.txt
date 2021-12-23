please downgrade the version of your setuptools by running the below command:

pip install -U setuptools==58.0.0

Otherwise this error will show:
WARNING: Discarding https://files.pythonhosted.org/packages/96/67/6db789e2533158963d4af689f961b644ddd9200615b8ce92d6cad695c65a/demjson-2.2.4.tar.gz#sha256=31de2038a0fdd9c4c11f8bf3b13fe77bc2a128307f965c8d5fb4dc6d6f6beb79 (from https://pypi.org/simple/demjson/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
ERROR: Could not find a version that satisfies the requirement demjson>=2.2.4 (from versions: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 2.0, 2.0.1, 2.2, 2.2.1, 2.2.2, 2.2.3, 2.2.4)
ERROR: No matching distribution found for demjson>=2.2.4

it is due to above versions of python setuptools broke the support for 2to3.
