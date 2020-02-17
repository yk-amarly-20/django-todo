from django import forms
from .models import Category

# フォームを実装


class AddTodo(forms.Form):
    """
    todoを新規追加
    title, categoryを追加
    """

    title = forms.CharField(
        label='タイトル',
        max_length=50,
        required=True
    )

    dead_line = forms.DateTimeField(
        label='締め切り',
        required=False,
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    category = forms.ModelMultipleChoiceField(
        label='カテゴリ',
        queryset=Category.objects.all()
    )
