from employeeapi.viewsets import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewset)

# localhost:8000/api
# GET, POST, PUT, DELETE
# GET -> list, retrive - localhost:8000/api/employee || localhost:8000/api/employee/3

