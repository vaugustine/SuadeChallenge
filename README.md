Requirements
------------

To install and run this application you need:

- Python 3

Install application
-------------------

The commands below installs the application and its dependencies:

    $ git clone https://github.com/vaugustine/SuadeChallenge.git
    $ cd SuadeChallenge
    $ python3 -m venv venv
    $ source venv/bin/activate
    (venv) pip install -r requirements.txt
    
cairo, Pango and GDK-PixBuf need to be installed separately. See platform-specific instructions to install these packages @
http://weasyprint.readthedocs.io/en/latest/install.html

Run application
---------------

The commands below runs the application:

    (venv) python run.py
    
Test application
---------------

The commands below runs the unit tests for the application:

    (venv) python test_reports.py
