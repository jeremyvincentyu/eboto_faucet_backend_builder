source bin/activate
export PYTHONPATH=$PYTHONPATH:src
python3 -m gunicorn -w 1 faucet:app -b 127.0.0.1:5003 --log-level debug