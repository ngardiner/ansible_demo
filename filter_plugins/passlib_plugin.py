# this ansible/jinja2 filter plugin allows you to use passlib's *_crypt functions
# until ansible 2.0 comes out - see https://github.com/ansible/ansible/issues/11244.
#
# this filter depends on passlib being installed:
# $ pip install passlib
#
# put this into your playbook's `filter_plugins` folder.
#
# usage example:
# - name: create user
#   user:
#     name: username
#     password: "{{ user_password | passlib_hash('sha512', user_salt) }}"

from ansible import errors

try:
    from passlib.hash import md5_crypt
except Exception, e:
    raise errors.AnsibleFilterError('passlib package is not installed')

def passlib_hash(pw, salt=None):
    return md5_crypt.encrypt(pw)

class FilterModule(object):
    def filters(self):
        return {
            'passlib_hash' : passlib_hash
        }
