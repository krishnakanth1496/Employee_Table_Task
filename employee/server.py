import grpc
from concurrent import futures
import time

# import the generated classes
import employee_pb2
import employee_pb2_grpc

# import the original calculator.py
import app

class InsertEmployeeServicer(employee_pb2_grpc.EmployeeServicer):

    def InsertEmployee(self, request, context):
        print("entered")
        response = employee_pb2.InsertEmployeeResponse()
        is_inserted = app.insert_employee(request)

        if is_inserted:
            response.message = "employee inserted successfully"
        else:
            response.message = "error while inserting"
        return response

class DeleteEmployeeServicer(employee_pb2_grpc.DeleteEmployeeServicer):

    def DeleteEmployee(self, request, context):
        response = employee_pb2.DeleteEmployeeResponse()
        is_deleted = app.delete_employee(request)
        print(is_deleted)
        if is_deleted:
            response.message = "employee deleted successfully"
        else:
            response.message = "error while deleting"
        return response

class UpdateEmployeeServicer(employee_pb2_grpc.UpdateEmployeeServicer):

    def UpdateEmployee(self, request, context):
        response = employee_pb2.UpdateEmployeeResponse()
        is_updated = app.update_employee(request)
        if is_updated:
            response.message = "employee updated successfully"

        else:
            response.message = "error while updating"

        return response

class SelectEmployeeServicer(employee_pb2_grpc.SelectEmployeeServicer):

    def SelectEmployee(self, request, context):
        response = employee_pb2.SelectEmployeeResponse()
        is_selected = app.select_employee(request.id)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

employee_pb2_grpc.add_EmployeeServicer_to_server(InsertEmployeeServicer(), server)

employee_pb2_grpc.add_DeleteEmployeeServicer_to_server(DeleteEmployeeServicer(), server)

employee_pb2_grpc.add_UpdateEmployeeServicer_to_server(UpdateEmployeeServicer(), server)

employee_pb2_grpc.add_SelectEmployeeServicer_to_server(SelectEmployeeServicer(), server)

# calculator_pb2_grpc.add_SubstractionServicer_to_server(SubstractionServicer(), server)
#
# calculator_pb2_grpc.add_MultiplicationServicer_to_server(MultiplicationServicer(), server)
#
# calculator_pb2_grpc.add_DivisionServicer_to_server(DivisionServicer(), server)

print('Starting server. Listening on port 50052.')
server.add_insecure_port('[::]:50052')
server.start()
server.wait_for_termination()

# try:
#     while True:
#         time.sleep(86400)
# except KeyboardInterrupt:
#     server.stop(0)