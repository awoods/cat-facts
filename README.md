# Cat Facts
## Sample project for exploring virtual environments

## Steps

### Initial setup
```bash
git clone git@github.com:awoods/cat-facts.git
cd cat-facts
pip freeze
python facts.py # (may or may not work, based on locally available dependencies)
python3.12 -m venv .venv
source .venv/bin/activate
pip freeze
python facts.py # (will not work)
pip install requests
pip freeze
clear; python facts.py # (success)
pip freeze > requirements.txt
deactivate
```

### Next time
```bash
cd cat-facts
source .venv/bin/activate
python facts.py
deactivate
```

### Start over as someone else
```
cd cat-facts
rm -rf .venv
python facts.py # (may or may not work)
python3.12 -m venv .venv
source .venv/bin/activate
python facts.py # (will not work)
pip install -r requirements.txt
python facts.py # (success)
```
