from django.shortcuts import render, redirect, get_object_or_404
from todo_list.models import Category, Todo
from .forms import AddTodo

# Create your views here.


def index(request):
    """
    全てのtodoを表示
    """
    todo = Todo.objects.order_by('title')

    return render(request, 'todo/index.html', {'todolist': todo})


def delete(request, id):
    """
    idを指定して、そのtodoを削除

    Parameters
    ----------
    id: int
        todoのid
    """

    todo = get_object_or_404(Todo, pk=id)
    todo.delete()

    return render(request, 'todo/delete.html')


def show_category(request):
    """
    カテゴリの一覧を表示　
    """

    category = Category.objects.all()

    return render(request, 'todo/category.html', {'categories': category})


def todo_category(request, category_name):
    """
    カテゴリを指定して、todoから絞り込み表示

    Parameters
    ----------
    category: string
        カテゴリ
    """

    category = Category.objects.get(title=category_name)
    todo = Todo.objects.filter(category=category).order_by('title')

    return render(request, 'todo/todo_category.html', {'todo_list': todo, 'category': category})
    # return render(request, 'todo/todo_category.html', {'todo_list': todo})


def add(request):
    """
    フォームから受け取ったtodoを作成
    """

    form = AddTodo(request.POST or None)
    if form.is_valid():
        todo = Todo()
        todo.title = form.cleaned_data['title']
        todo.dead_line = form.cleaned_data['dead_line']
        category = form.cleaned_data['category']

        category = category.get()
        print(type(category))
        Todo.objects.create(
            title=todo.title,
            dead_line=todo.dead_line,
            created_at=todo.created_at
        )

        todo.category.set(category)

        return redirect('todo_list:index')
    return render(request, 'todo/add.html', {'form': form})
