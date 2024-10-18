from django import forms
from .models import List

class AddTasks(forms.ModelForm):
    task_name = forms.CharField(required = True, widget= forms.widgets.TextInput(attrs={"placeholder":"Task Name", "class":"form-control"}), label="")
    description = forms.CharField( widget= forms.widgets.Textarea(attrs={"placeholder":"Description", "class":"form-control"}), label="")
    complete = forms.BooleanField(required=False, label="Task Status ")


    class Meta:
        exclude = ("user",)
        model = List

    def save(self, commit=True, user=None):
        task = super().save(commit=False)
        if user:
            task.user = user  # Bind the task to the user
        if commit:
            task.save()
        return task


    # def form_valid(self, form):
    #     form.instance = self.request.user
    #     form.save()
    #     return super().form_valid(form)
    