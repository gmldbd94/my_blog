from django import forms
from . import models
from phonenumber_field.modelfields import PhoneNumberField


# class BlogForm(forms.ModelForm):
#     title = forms.CharField(label="제목", widget=forms.TextInput(attrs={"placeholder": "제목을 입력하시오"}))
#     context = forms.CharField(required=True, label="내용", widget=forms.Textarea(attrs={"placeholder": "내용을 입력하시오"}))
#     class Meta:
#         model = Blog
#         fields = [
#             'title',
#             'context',
#         ]
#
#     def clean_context(self):
#         context = self.cleaned_data.get("context")
#         if context == None:
#             raise forms.ValidationError("내용울 입력하시오")
#         return context

class NoteForm(forms.ModelForm):
    title = forms.CharField(label="제목", widget=forms.TextInput())
    file = forms.FileField(label="파일첨부")
    content = forms.CharField(label="내용", widget=forms.Textarea())
    category = forms.CharField(label="카테고리", widget=forms.ChoiceField())
    link = forms.URLField(label="링크", widget=forms.URLField())

    class Meta:
        model = models.Note
        fields = ['title',
                  'content',
                  'file',
                  'category',
                  'link',
                  ]

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="댓글", widget=forms.Textarea())

    class Meta:
        model = models.Comment
        fields = ['content']

class mentorForm(forms.ModelForm):
    name = forms.CharField(label="이름", widget=forms.TextInput)
    content = forms.CharField(label="자기소개 및 상담내용", widget=forms.Textarea)
    email = forms.EmailField(label="이메일", widget=forms.EmailInput)
    phone = forms.CharField(label="핸드폰 번호", widget=forms.TextInput)

    class Meta:
        model = models.mentor
        fields = ['name',
                  'conent',
                  'email',
                  'phone',
                  ]