from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student

# 顯示學生列表
class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'

# 建立學生資料
class StudentCreateView(CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'age', 'student_id']
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student-list')

# 更新學生資訊
class StudentUpdateView(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'age', 'student_id']
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student-list')

# 刪除學生
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')
