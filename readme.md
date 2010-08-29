# Usefull tools for developing on Google App Engine

* JsonProperty for datastore
* Base32 encoded UUID

# Usage

    git clone git@github.com:deck/gae-utils.git gaeUtils

or

    git submodule add git@github.com:deck/gae-utils.git gaeUtils

## JsonProperty

from google.appengine.ext import db
from gaeUtils.datastore_properties import JsonProperty

    class Note(db.Model):
        data = JsonProperty()


## Encoded UUID

    from gaeUtils.util import generate_key

    unique_id = generate_key()
