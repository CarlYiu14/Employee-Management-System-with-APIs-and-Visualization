from django.shortcuts import render
from employees.models import Employee, Department
from attendance.models import Attendance
from django.db.models import Count
from datetime import date, timedelta
from collections import Counter

def chart_view(request):
    # Pie chart data: Employee Department Distribution
    dept_counts = Employee.objects.values('department__name').annotate(total=Count('id'))
    department_data = {
        'labels': [d['department__name'] for d in dept_counts],
        'data': [d['total'] for d in dept_counts]
    }

    # Bar chart data: Recent 6 months attendance status
    today = date.today()
    months = [(today.replace(day=1) - timedelta(days=30*i)).strftime('%Y-%m') for i in range(5, -1, -1)]
    month_counter = Counter()

    for month in months:
        count = Attendance.objects.filter(
            date__startswith=month,
            status='Present'
        ).count()
        month_counter[month] = count

    attendance_data = {
        'labels': list(month_counter.keys()),
        'data': list(month_counter.values())
    }

    return render(request, 'charts.html', {
        'department_data': department_data,
        'attendance_data': attendance_data
    })
