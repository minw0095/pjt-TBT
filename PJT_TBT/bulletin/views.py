from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from products.models import Product
from django.http import JsonResponse

# Create your views here.


def create(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.account = request.user
            question.name = product
            question.save()
            return redirect("products:products_detail", product_pk)
    else:
        form = QuestionForm()
    context = {"form": form}
    return redirect("products:products_detail", product_pk)
    # return render(request, "bulletin/create.html", context)


def detail(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    question = product.question_set.all()
    context = {"question": question}
    return render(request, "bulletin/detail.html", context)


def delete(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    product_pk = question.name_id
    if request.user.pk == question.account.pk:
        question.delete()
    return redirect("products:products_detail", product_pk)


# def update(
#     request,
#     question_pk,
# ):
#     question = Question.objects.get(pk=question_pk)
#     questionForm = list(Question.objects.values())
#     product_pk = question.name
#     is_pass = False
#     if request.user.pk == question.account.pk:
#         if request.method == "POST":
#             form = QuestionForm()(request.POST, instance=question)
#             if form.is_valid():
#                 form.save()
#                 return redirect("products:products_detail", product_pk)
#         else:
#             form = QuestionForm(instance=question)
#             questionForm = form.values()
#             return JsonResponse(context={"isPass": is_pass})
#         # context = {"form": form}
#     else:
#         # return redirect("products:index")
#         return JsonResponse(context={"isPass": is_pass})
#     return JsonResponse(context={"isPass": is_pass})
# return render(request, "bulletin/update.html", context)


# Answer 쪽 crud
def createA(request, question_pk):
    question = Question.objects.get(pk=question_pk)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.account = request.user
            answer.save()
            if question.answer_set.exists():
                question.check = True
                question.save()
            return redirect("products:index")
    else:
        form = AnswerForm()
    context = {"form": form}
    return render(request, "bulletin/createA.html", context)


def deleteA(request, answer_pk):
    answer = Answer.objects.get(pk=answer_pk)
    if request.user.pk == answer.account.pk:
        answer.delete()
    return redirect("products:index")


def updateA(
    request,
    answer_pk,
):
    answer = Answer.objects.get(pk=answer_pk)
    if request.user.pk == answer.account.pk:
        if request.method == "POST":
            form = AnswerForm()(request.POST, instance=answer)
            if form.is_valid():
                form.save()
                return redirect("products:index")
        else:
            form = AnswerForm(instance=answer)
        context = {"form": form}
    else:
        return redirect("products:index")
    return render(request, "bulletin/updateA.html", context)
