from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView,  UpdateView
from .models import Profile
from .forms import ProfileForm
from django import forms
from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont
import pandas as pd


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('myauth:login')


class MainView(TemplateView):
    model = Profile
    template_name = "myauth/main.html"


class CalculatorView(TemplateView):
    template_name = "myauth/calculator.html"


def registration(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        form2 = ProfileForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print("Зашел")
            form1.save()
            form2.save()
            # получаем имя пользователя и пароль из формы
            username = form1.cleaned_data.get('username')
            password = form1.cleaned_data.get('password1')
            name = form2.cleaned_data.get('name')
            surname = form2.cleaned_data.get('surname')
            middle_name = form2.cleaned_data.get('middle_name')
            email = form2.cleaned_data.get('email')
            organization = form2.cleaned_data.get('organization')
            inn = form2.cleaned_data.get('inn')
            site = form2.cleaned_data.get('site')
            branch = form2.cleaned_data.get('branch')
            country = form2.cleaned_data.get('country')
            city = form2.cleaned_data.get('city')
            position = form2.cleaned_data.get('position')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            login(request, user)
            Profile.objects.create(user=request.user, name=name, surname=surname, middle_name=middle_name,
                                   email=email, organization=organization, inn=inn, site=site, branch=branch,
                                   country=country, city=city, position=position)
            return render(request, 'myauth/main.html')
    else:
        form1 = UserCreationForm()
        form2 = ProfileForm()
    return render(request, 'myauth/register.html', {'form1': form1, 'form2': form2})


class ProfileDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        profile = Profile.objects.get(user=request.user)
        context = {
            "profile": profile
        }
        return render(request, 'myauth/profile.html', context=context)


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm

    def form_valid(self, form: forms.Form):
        if form.is_valid():
            return super(ProfileUpdateView, self).form_valid(form)
        return self.form_invalid(form)

    def get_success_url(self):
        return reverse('myauth:profile', kwargs={'pk': self.object.id})


def downlaod_pdf(request: HttpRequest):
    image_3()
    image_4()
    make_pdf()
    with open('myauth/application/pdf/result.pdf', 'rb') as f:
        file_data = f.read()

    response = HttpResponse(file_data, content_type='application/pdf')
    response['Content-Disposition'] = "attachment; filename=Result.pdf"
    return response


def image_3(path='myauth/application/images/3.jpg'): #Здесь данные для 3 страницы
    im = Image.open(path)
    font = ImageFont.truetype("myauth/font/Roboto-Regular.ttf", 64, encoding='UTF-8')
    draw_text = ImageDraw.Draw(im)

    branch = "Авиационная промышленность"
    draw_text.text((1200, 560), branch, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    org_type = "ИП"
    draw_text.text((1600, 770), org_type, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    employees_count = "{} человек".format(20)
    draw_text.text((1500, 1120), employees_count, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    district = "ЦАО"
    draw_text.text((1580, 1380), district, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    min_total_expenses = 100
    max_total_expenses = 300
    draw_text.text((1300, 1800), "От {} до {} млн.руб.".format(min_total_expenses, max_total_expenses),
                   fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    employees_expenses = "{} млн.руб.".format(20)
    draw_text.text((1500, 2190), employees_expenses, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    rent_expenses = "{} млн.руб.".format(140)
    draw_text.text((1500, 2410), rent_expenses, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    taxes_expenses = "{} млн.руб.".format(20)
    draw_text.text((1500, 2610), taxes_expenses, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    services_expenses = "{} млн.руб.".format(20)
    draw_text.text((1500, 2800), services_expenses, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    im.save('myauth/application/images/3_1.jpg')


def image_4(path='myauth/application/images/4.jpg'): #Здесь данные для 4 страницы
    im = Image.open(path)
    font = ImageFont.truetype("myauth/font/Roboto-Regular.ttf", 64, encoding='UTF-8')
    draw_text = ImageDraw.Draw(im)

    min_totals = 100
    max_totals = 300
    draw_text.text((1400, 1910), text="От {} до {} млн.руб.".format(min_totals, max_totals),
                   fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    employees_count = 20
    draw_text.text((1550, 2170), "{} человек ".format(employees_count), fill=('#1C0606'),
                   font=font, stroke_width=1, stroke_fill="black")

    min_pensionary_expenses = 10
    max_pensionary_expenses = 100
    draw_text.text((1400, 2430), "От {} до {} млн.руб. ".format(min_pensionary_expenses, max_pensionary_expenses),
                   fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    min_health_expenses = 10
    max_health_expenses = 100
    draw_text.text((1400, 2700), "От {} до {} млн.руб. ".format(min_health_expenses, max_health_expenses),
                   fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")

    im.save('myauth/application/images/4_1.jpg')


def make_pdf():
    pdf = FPDF(format='A4')
    pdf.add_page()
    pdf.image('myauth/application/images/1.jpg', x=0, y=0, w=211)
    pdf.add_page()
    pdf.image('myauth/application/images/2.jpg', x=0, y=0, w=211)
    pdf.add_page()
    pdf.image('myauth/application/images/3_1.jpg', x=0, y=0, w=211)
    pdf.add_page()
    pdf.image('myauth/application/images/4_1.jpg', x=0, y=0, w=211)
    pdf.output("myauth/application/pdf/result.pdf")


def download_excel(request): #Скачать excel
    #Первый лист
    branch = "Авиационная промышленность"
    org_type = "ИП"
    employees_count = "{} человек".format(20)
    district = "ЦАО"
    organization_info = pd.DataFrame({'Наименование': ['Отрасль', 'Тип организации', 'Количество сотрудников',
                                                       'Район расположения производства'],
                                      'Значение': [branch, org_type, employees_count, district]})
    #Второй лист
    min_total_expenses = 100
    max_total_expenses = 300
    employees_expenses = "{} млн.руб.".format(20)
    rent_expenses = "{} млн.руб.".format(140)
    taxes_expenses = "{} млн.руб.".format(20)
    services_expenses = "{} млн.руб.".format(20)
    possible_costs = pd.DataFrame(
        {'Наименование': ['Персонал', 'Аренда объектов недвижимости',
                          'Налоги', 'Услуги', 'Итого возможных расходов'],
            'Значение': [employees_expenses, rent_expenses, taxes_expenses, services_expenses,
                         "От {} до {} млн.руб.".format(min_total_expenses, max_total_expenses)]})
    #Третий лист
    min_totals = 100
    max_totals = 300
    employees_count = 20
    min_pensionary_expenses = 10
    max_pensionary_expenses = 100
    min_health_expenses = 10
    max_health_expenses = 100
    organization_personal = pd.DataFrame(
        {'Наименование': ['Итого возможных расходов на содержание персонала организации',
                          'Планируемая численность персонала', 'Страховые взносы(пенсионное страхование)',
                          'Страховые взносы(медицинское страхование)'],
        'Значение': ["От {} до {} млн.руб.".format(min_totals, max_totals), "{} человек ".format(employees_count),
                     "От {} до {} млн.руб.".format(min_pensionary_expenses, max_pensionary_expenses),
                     "От {} до {} млн.руб.".format(min_health_expenses, max_health_expenses)]})
    writer = pd.ExcelWriter('myauth/application/ms-excel/result.xlsx', engine='xlsxwriter')

    #Названия листов
    info_sheets = {'Информация о вашей организации': organization_info,
                   'Итоговые возможные затраты': possible_costs,
                   'Персонал организации': organization_personal}

    #Заполнение excel
    for sheetname, df in info_sheets.items():
        df.to_excel(writer, sheet_name=sheetname, index=False)
        worksheet = writer.sheets[sheetname]
        for idx, col in enumerate(df):
            series = df[col]
            max_len = max(series.astype(str).map(len).max(), len(str(series.name))) + 10
            worksheet.set_column(idx, idx, max_len)
    writer.close()

    with open('myauth/application/ms-excel/result.xlsx', 'rb') as f:
        file_data = f.read()
    response = HttpResponse(file_data, content_type='application/ms-excel')
    response['Content-Disposition'] = "attachment; filename=Result.xlsx"

    return response

