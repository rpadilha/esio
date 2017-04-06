from django import forms
from s3direct.widgets import S3DirectWidget


class S3DirectUploadForm(forms.Form):
    picture = forms.URLField(widget=S3DirectWidget(dest='AmazonS3'))


class BlogSearchForm(forms.Form):
    search = forms.CharField(max_length="50", required=True)
