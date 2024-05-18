#### create venv

python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt

.
├── README.md
├── ii.py
├── lib
│   └── uptime.py
└── requirements.txt

❯ ./ii.py
Usage: ii.py [OPTIONS] COMMAND [ARGS]...

  A simple CLI example

Options:
  --help  Show this message and exit.

Commands:
  read-file  Read and print the contents of a file
  uptime