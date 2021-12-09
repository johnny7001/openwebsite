from django import forms #表單功能
from captcha.fields import CaptchaField
from userdata.models import Diary
from message.models import Post
class ContactForm(forms.Form):
    CITY = [
        ['TP', 'Taipei'],
        ['TY', 'Taoyuang'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
        ['KS', 'Kaohsiung'],
        ['NA', 'Others'],
    ]
    user_name = forms.CharField(label='你的姓名', max_length=50, initial='Tseng') #initial=預設值
    user_city = forms.ChoiceField(label='居住城市', choices=CITY) #下拉是選單
    user_school = forms.BooleanField(label='是否在學', required=False) #此欄位不一定要勾選
    user_email = forms.EmailField(label='電子郵件')
    user_message = forms.CharField(label='你的意見', widget=forms.Textarea) #Textarea = 大量文字輸入的欄位

class PostForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Post
        fields = ['mood', 'nickname', 'message', 'del_pass']

    def __init__(self, *args, **kwargs): #將預設英文欄位名稱
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = '現在心情'
        self.fields['nickname'].label = '你的暱稱'
        self.fields['message'].label = '心情留言'
        self.fields['del_pass'].label = '設定密碼'
        self.fields['captcha'].label = '確定你不是機器人'

class LoginForm(forms.Form):
    username = forms.CharField(label='姓名', max_length=10)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())




class DateInput(forms.DateInput): #日期表單
    input_type = 'date'

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['budget', 'weight', 'note', 'ddate']
        widgets = {'ddate': DateInput(),} #wedgets=附件

    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['budget'].label = '今日花費(元)'
        self.fields['weight'].label = '今日體重(kg)'
        self.fields['note'].label = '心情留言'
        self.fields['ddate'].label = '日期'




# class LoginForm(forms.Form):
#     COLORS = [
#         ['紅', '紅'],
#         ['黃', '黃'],
#         ['綠', '綠'],
#         ['藍', '藍'],
#         ['紫', '紫'],
#     ]
#     user_name = forms.CharField(label='你的名字', max_length=10)
#     user_color = forms.ChoiceField(label='幸運顏色', choices=COLORS)  # 下拉選單
