"""Create single import location for v2c and v1 protocols

These can get moved around inside PySNMP, so we need this
code to determine where the prototypes are, so we can reliably
and simply import them throughout TwistedSNMP.
"""
try:
	from pysnmp.proto import v2c, v1, error, rfc1155, rfc1902
	from pysnmp.asn1 import univ
	# generic appears to have side effects we need...
	from pysnmp.proto.api import generic
except ImportError, err:
	from pysnmp.v4.proto.omni import v2c,v1, error, rfc1157, rfc1905
	
try:
	raise ImportError
	import psyco
except ImportError, err:
	pass
else:
	from pysnmp.asn1 import base
	psyco.bind(base.SimpleAsn1Object)
	psyco.bind(base.Asn1Object)
	psyco.bind(base.FixedTypeAsn1Object)
	psyco.bind(base.RecordTypeAsn1Object)
	psyco.bind(base.ChoiceTypeAsn1Object)
	psyco.bind(base.AnyTypeAsn1Object)
	psyco.bind(base.VariableTypeAsn1Object)
	from pysnmp.asn1.encoding.ber import base
	psyco.bind(base.BerObject)
	psyco.bind(base.SimpleAsn1Object)
	psyco.bind(base.StructuredAsn1Object)
	psyco.bind(base.FixedTypeAsn1Object)
	psyco.bind(base.OrderedFixedTypeAsn1Object)
	psyco.bind(base.UnorderedFixedTypeAsn1Object)
	psyco.bind(base.SingleFixedTypeAsn1Object)
	psyco.bind(base.VariableTypeAsn1Object)
	psyco.bind(univ.ObjectIdentifier)
	# now clean up the namespace...
	del base
	del psyco

try:
	from pysnmp.asn1 import oid
	USE_STRING_OIDS = False
	# This seems to slow down rather than speed up the OID class...
	#psyco.bind(oid.OID)
except ImportError, err:
	from twistedsnmp import oid
	USE_STRING_OIDS = True

def cacheOIDEncoding( oid ):
	"""Null operation when no univ module available"""
try:
	from pysnmp.asn1.encoding.ber import univ
	cacheOIDEncoding = univ.ObjectIdentifierMixIn.berInternEncoding
	CAN_CACHE_OIDS = True
except (ImportError,AttributeError), err:
	CAN_CACHE_OIDS = False
