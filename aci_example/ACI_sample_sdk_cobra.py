# /usr/bin/env python3
from credentials import *
import cobra.mit.session
import cobra.mit.access
import cobra.mit.request

auth = cobra.mit.session.LoginSession(URL, LOGIN, PASSWORD)
session = cobra.mit.access.MoDirectory(auth)
session.login()

tenant_query = cobra.mit.request.DnQuery("uni/tn-Heroes")
heroes_tenant = session.query(tenant_query)
heroes = heroes_tenant[0]
print(heroes.name)
print(heroes.dn)
