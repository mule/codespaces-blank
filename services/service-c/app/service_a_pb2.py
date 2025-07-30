from service_c.service_a_pb2 import *

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fservice_a.proto\x12\tservice_a\"\x1a\n\x07Request\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1a\n\x08Response\x12\x0e\n\x06result\x18\x01 \x01(\t2B\n\x08ServiceA\x12\x36\n\x0b\x43\x61llService\x12\x12.service_a.Request\x1a\x13.service_a.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_a_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REQUEST']._serialized_start=30
  _globals['_REQUEST']._serialized_end=56
  _globals['_RESPONSE']._serialized_start=58
  _globals['_RESPONSE']._serialized_end=84
  _globals['_SERVICEA']._serialized_start=86
  _globals['_SERVICEA']._serialized_end=152
# @@protoc_insertion_point(module_scope)
