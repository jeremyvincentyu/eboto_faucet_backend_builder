python3 -m venv eboto_faucet_backend_runtime
rsync -urv eboto_faucet_backend_builder/src/ eboto_faucet_backend_runtime/src/
cp eboto_faucet_backend_builder/deploy.sh eboto_faucet_backend_runtime/
cp eboto_faucet_backend_builder/requirements.txt eboto_faucet_backend_runtime/
cd eboto_faucet_backend_runtime
source bin/activate
pip install -r requirements.txt
mkdir data
mkdir data/voter_logs
mkdir data/voter_keys