import os
import urllib.request as req
from urllib.parse import urlparse


def download(url, to=None):
    """Download a remote file specified by a URL to a
    local directory.

    :param url: str
      URL pointing to a remote file.

    :param to: str
      Local path, absolute or relative, with a filename
      to the file storing the contents of the remote file.
    """

    # TODO: Implement me!
    real_url = urlparse(url)
    r_url = url.split("/")
    if real_url:
        if to:
            os.chdir(to)
            req.urlretrieve(url, r_url[-1])
            os.chdir("./")
        else:
            req.urlretrieve(url, r_url[-1])
    pass
