
"""
Perform a query in arXiv about papers useful to the user and send email with results

NOTE: as it uses urllib2, it only works on Python3.x
"""

# ------------------------------------------------------------------------------------------
# IDEA:
# I) User specifies keywords/autho name/title, whatever,
# II) Use API for query,
# III) Parse results into some nice human-readable format,
# IV) Email result at an specified time of the day.
# ------------------------------------------------------------------------------------------

import os
import smtplib
import sys
from email.mime.text import MIMEText
import feedparser
from urllib2 import urlopen

__authors__ = ["Gastón Escobar", "Federico Fogantini", "Adolfo Simaz Bunzel"]
__credits__ = ["Gastón Escobar", "Federico Fogantini", "Adolfo Simaz Bunzel"]
__license__ = "GPL"
__version__ = "1.0"
__maintainers__ = ["Gastón Escobar", "Federico Fogantini", "Adolfo Simaz Bunzel"]
__email__ = ["asimazbunzel@iar.unlp.edu.ar"]


# ------------------------------------------------------------------------------------------
class Paper:
    """
    Empty docstring for Paper class.

    Parameters
    ----------
    TBD

    Returns
    -------
    TBD

    Usage
    -----
    TBD
    """
    def __init__(self,
                 arxiv_id,
                 title,
                 first_author,
                 keywords,
                 url):

        self.arxiv_id = arxiv_id
        self.title = title
        self.first_author = first_author
        self.keywords = keywords  # list-type
        self.url = url


def astro_query():
    """
    Do actual query using arXiv API.

    Parameters
    ----------
    TBD

    Returns
    -------
    TBD

    Usage
    -----
    TBD
    """

def send_mail():
    """
    Send email to user specified

    Parameters
    ----------
    TBD

    Returns
    -------
    TBD

    Usage
    -----
    TBD
    """
    from = 'asimazbunzel@localhost <asb test>'
    to = 'asimazbunzel@gmail.com'
    msg = MIMEMultipart()
    msg['From'] = from
    msg['To'] = to
    msg['Subject'] = subject

    body = 'paper-info'
    msg.attach(MIMEText(body, 'plain'))

    try:
        smt = smtplib.SMTP('localhost')
        smt.sendmail(from, to, msg.as_string())
    except smtplib.SMTPException:
        sys.exit("ERROR sending mail")
