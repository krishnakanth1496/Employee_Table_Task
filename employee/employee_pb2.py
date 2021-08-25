# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: employee.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='employee.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x65mployee.proto\"Q\n\x15InsertEmployeeRequest\x12\x14\n\x0c\x65mployeeName\x18\x01 \x01(\t\x12\x0e\n\x06salary\x18\x02 \x01(\x01\x12\x12\n\ndepartment\x18\x03 \x01(\t\")\n\x16InsertEmployeeResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"#\n\x15\x44\x65leteEmployeeRequest\x12\n\n\x02id\x18\x01 \x01(\x05\")\n\x16\x44\x65leteEmployeeResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"]\n\x15UpdateEmployeeRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x14\n\x0c\x65mployeeName\x18\x02 \x01(\t\x12\x0e\n\x06salary\x18\x03 \x01(\x01\x12\x12\n\ndepartment\x18\x04 \x01(\t\")\n\x16UpdateEmployeeResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"#\n\x15SelectEmployeeRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"^\n\x16SelectEmployeeResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x14\n\x0c\x65mployeeName\x18\x02 \x01(\t\x12\x0e\n\x06salary\x18\x03 \x01(\x01\x12\x12\n\ndepartment\x18\x04 \x01(\t2O\n\x08\x45mployee\x12\x43\n\x0eInsertEmployee\x12\x16.InsertEmployeeRequest\x1a\x17.InsertEmployeeResponse\"\x00\x32U\n\x0e\x44\x65leteEmployee\x12\x43\n\x0e\x44\x65leteEmployee\x12\x16.DeleteEmployeeRequest\x1a\x17.DeleteEmployeeResponse\"\x00\x32U\n\x0eUpdateEmployee\x12\x43\n\x0eUpdateEmployee\x12\x16.UpdateEmployeeRequest\x1a\x17.UpdateEmployeeResponse\"\x00\x32U\n\x0eSelectEmployee\x12\x43\n\x0eSelectEmployee\x12\x16.SelectEmployeeRequest\x1a\x17.SelectEmployeeResponse\"\x00\x62\x06proto3'
)




_INSERTEMPLOYEEREQUEST = _descriptor.Descriptor(
  name='InsertEmployeeRequest',
  full_name='InsertEmployeeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='employeeName', full_name='InsertEmployeeRequest.employeeName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='salary', full_name='InsertEmployeeRequest.salary', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='department', full_name='InsertEmployeeRequest.department', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=99,
)


_INSERTEMPLOYEERESPONSE = _descriptor.Descriptor(
  name='InsertEmployeeResponse',
  full_name='InsertEmployeeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='InsertEmployeeResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=142,
)


_DELETEEMPLOYEEREQUEST = _descriptor.Descriptor(
  name='DeleteEmployeeRequest',
  full_name='DeleteEmployeeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='DeleteEmployeeRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=179,
)


_DELETEEMPLOYEERESPONSE = _descriptor.Descriptor(
  name='DeleteEmployeeResponse',
  full_name='DeleteEmployeeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='DeleteEmployeeResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=222,
)


_UPDATEEMPLOYEEREQUEST = _descriptor.Descriptor(
  name='UpdateEmployeeRequest',
  full_name='UpdateEmployeeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UpdateEmployeeRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='employeeName', full_name='UpdateEmployeeRequest.employeeName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='salary', full_name='UpdateEmployeeRequest.salary', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='department', full_name='UpdateEmployeeRequest.department', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=317,
)


_UPDATEEMPLOYEERESPONSE = _descriptor.Descriptor(
  name='UpdateEmployeeResponse',
  full_name='UpdateEmployeeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='UpdateEmployeeResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=360,
)


_SELECTEMPLOYEEREQUEST = _descriptor.Descriptor(
  name='SelectEmployeeRequest',
  full_name='SelectEmployeeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SelectEmployeeRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=362,
  serialized_end=397,
)


_SELECTEMPLOYEERESPONSE = _descriptor.Descriptor(
  name='SelectEmployeeResponse',
  full_name='SelectEmployeeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SelectEmployeeResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='employeeName', full_name='SelectEmployeeResponse.employeeName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='salary', full_name='SelectEmployeeResponse.salary', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='department', full_name='SelectEmployeeResponse.department', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=399,
  serialized_end=493,
)

DESCRIPTOR.message_types_by_name['InsertEmployeeRequest'] = _INSERTEMPLOYEEREQUEST
DESCRIPTOR.message_types_by_name['InsertEmployeeResponse'] = _INSERTEMPLOYEERESPONSE
DESCRIPTOR.message_types_by_name['DeleteEmployeeRequest'] = _DELETEEMPLOYEEREQUEST
DESCRIPTOR.message_types_by_name['DeleteEmployeeResponse'] = _DELETEEMPLOYEERESPONSE
DESCRIPTOR.message_types_by_name['UpdateEmployeeRequest'] = _UPDATEEMPLOYEEREQUEST
DESCRIPTOR.message_types_by_name['UpdateEmployeeResponse'] = _UPDATEEMPLOYEERESPONSE
DESCRIPTOR.message_types_by_name['SelectEmployeeRequest'] = _SELECTEMPLOYEEREQUEST
DESCRIPTOR.message_types_by_name['SelectEmployeeResponse'] = _SELECTEMPLOYEERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InsertEmployeeRequest = _reflection.GeneratedProtocolMessageType('InsertEmployeeRequest', (_message.Message,), {
  'DESCRIPTOR' : _INSERTEMPLOYEEREQUEST,
  '__module__' : 'employee_pb2'
  # @@protoc_insertion_point(class_scope:InsertEmployeeRequest)
  })
_sym_db.RegisterMessage(InsertEmployeeRequest)

InsertEmployeeResponse = _reflection.GeneratedProtocolMessageType('InsertEmployeeResponse', (_message.Message,), {
  'DESCRIPTOR' : _INSERTEMPLOYEERESPONSE,
  '__module__' : 'employee_pb2'
  # @@protoc_insertion_point(class_scope:InsertEmployeeResponse)
  })
_sym_db.RegisterMessage(InsertEmployeeResponse)

DeleteEmployeeRequest = _reflection.GeneratedProtocolMessageType('DeleteEmployeeRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEEMPLOYEEREQUEST,
  '__module__' : 'employee_pb2'
  # @@protoc_insertion_point(class_scope:DeleteEmployeeRequest)
  })
_sym_db.RegisterMessage(DeleteEmployeeRequest)

DeleteEmployeeResponse = _reflection.GeneratedProtocolMessageType('DeleteEmployeeResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEEMPLOYEERESPONSE,
  '__module__' : 'employee_pb2'
  # @@protoc_insertion_point(class_scope:DeleteEmployeeResponse)
  })
_sym_db.RegisterMessage(DeleteEmployeeResponse)

UpdateEmployeeRequest = _reflection.GeneratedProtocolMessageType('UpdateEmployeeRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEEMPLOYEEREQUEST,
  '__module__' : 'employee_pb2'
  # @@protoc_insertion_point(class_scope:UpdateEmployeeRequest)
  })
_sym_db.RegisterMessage(UpdateEmployeeRequest)

UpdateEmployeeResponse = _reflection.GeneratedProtocolMessageType('UpdateEmployeeResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEEMPLOYEERESPONSE,
  '__module__' : 'employee_pb2'
  # @@protoc_insertion_point(class_scope:UpdateEmployeeResponse)
  })
_sym_db.RegisterMessage(UpdateEmployeeResponse)

SelectEmployeeRequest = _reflection.GeneratedProtocolMessageType('SelectEmployeeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SELECTEMPLOYEEREQUEST,
  '__module__' : 'employee_pb2'
  # @@protoc_insertion_point(class_scope:SelectEmployeeRequest)
  })
_sym_db.RegisterMessage(SelectEmployeeRequest)

SelectEmployeeResponse = _reflection.GeneratedProtocolMessageType('SelectEmployeeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SELECTEMPLOYEERESPONSE,
  '__module__' : 'employee_pb2'
  # @@protoc_insertion_point(class_scope:SelectEmployeeResponse)
  })
_sym_db.RegisterMessage(SelectEmployeeResponse)



_EMPLOYEE = _descriptor.ServiceDescriptor(
  name='Employee',
  full_name='Employee',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=495,
  serialized_end=574,
  methods=[
  _descriptor.MethodDescriptor(
    name='InsertEmployee',
    full_name='Employee.InsertEmployee',
    index=0,
    containing_service=None,
    input_type=_INSERTEMPLOYEEREQUEST,
    output_type=_INSERTEMPLOYEERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EMPLOYEE)

DESCRIPTOR.services_by_name['Employee'] = _EMPLOYEE


_DELETEEMPLOYEE = _descriptor.ServiceDescriptor(
  name='DeleteEmployee',
  full_name='DeleteEmployee',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=576,
  serialized_end=661,
  methods=[
  _descriptor.MethodDescriptor(
    name='DeleteEmployee',
    full_name='DeleteEmployee.DeleteEmployee',
    index=0,
    containing_service=None,
    input_type=_DELETEEMPLOYEEREQUEST,
    output_type=_DELETEEMPLOYEERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DELETEEMPLOYEE)

DESCRIPTOR.services_by_name['DeleteEmployee'] = _DELETEEMPLOYEE


_UPDATEEMPLOYEE = _descriptor.ServiceDescriptor(
  name='UpdateEmployee',
  full_name='UpdateEmployee',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=663,
  serialized_end=748,
  methods=[
  _descriptor.MethodDescriptor(
    name='UpdateEmployee',
    full_name='UpdateEmployee.UpdateEmployee',
    index=0,
    containing_service=None,
    input_type=_UPDATEEMPLOYEEREQUEST,
    output_type=_UPDATEEMPLOYEERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_UPDATEEMPLOYEE)

DESCRIPTOR.services_by_name['UpdateEmployee'] = _UPDATEEMPLOYEE


_SELECTEMPLOYEE = _descriptor.ServiceDescriptor(
  name='SelectEmployee',
  full_name='SelectEmployee',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=750,
  serialized_end=835,
  methods=[
  _descriptor.MethodDescriptor(
    name='SelectEmployee',
    full_name='SelectEmployee.SelectEmployee',
    index=0,
    containing_service=None,
    input_type=_SELECTEMPLOYEEREQUEST,
    output_type=_SELECTEMPLOYEERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SELECTEMPLOYEE)

DESCRIPTOR.services_by_name['SelectEmployee'] = _SELECTEMPLOYEE

# @@protoc_insertion_point(module_scope)