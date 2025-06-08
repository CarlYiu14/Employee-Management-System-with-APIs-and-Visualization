from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from employees.models import Employee, Department
from django.urls import reverse
from datetime import date

class EmployeeAPITests(APITestCase):

    def setUp(self):
        # create user and token
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # create department
        self.department = Department.objects.create(name="HR")

    def test_create_employee(self):
        url = reverse('employee-list')  # router name: <model>-list
        data = {
            "name": "Alice",
            "email": "alice@example.com",
            "phone": "1234567890",
            "address": "123 Main St",
            "date_joined": str(date.today()),
            "department_id": self.department.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Employee.objects.count(), 1)

    def test_get_employees_list(self):
        Employee.objects.create(
            name="Bob",
            email="bob@example.com",
            phone="9876543210",
            address="Somewhere",
            date_joined=date.today(),
            department=self.department
        )
        url = reverse('employee-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_token_authentication_required(self):
        # Test request without token
        client = APIClient()
        url = reverse('employee-list')
        response = client.get(url)
        self.assertEqual(response.status_code, 401)
