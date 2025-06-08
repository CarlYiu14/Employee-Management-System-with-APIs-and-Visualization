from django.core.management.base import BaseCommand
from employees.models import Employee, Department
from attendance.models import Attendance, Performance
from faker import Faker
import random
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seed the database with fake employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear existing data
        Attendance.objects.all().delete()
        Performance.objects.all().delete()
        Employee.objects.all().delete()
        Department.objects.all().delete()

        # Create Departments
        departments = []
        for dept_name in ['Engineering', 'HR', 'Marketing', 'Sales', 'Finance']:
            d = Department.objects.create(name=dept_name)
            departments.append(d)

        # Create Employees
        employees = []
        for _ in range(40):
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                date_joined=fake.date_between(start_date='-2y', end_date='today'),
                department=random.choice(departments)
            )
            employees.append(emp)

        # Create Attendance and Performance
        for emp in employees:
            for i in range(10):  # 10 attendance records per employee
                Attendance.objects.create(
                    employee=emp,
                    date=timezone.now().date() - timedelta(days=random.randint(1, 60)),
                    status=random.choice(['Present', 'Absent', 'Late'])
                )

            for i in range(3):  # 3 performance reviews per employee
                Performance.objects.create(
                    employee=emp,
                    rating=random.randint(1, 5),
                    review_date=timezone.now().date() - timedelta(days=random.randint(30, 365))
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with fake data.'))
