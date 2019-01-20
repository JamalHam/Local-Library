from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.
    
from django import forms

#book renewal form
class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise validationError(_('Invalid date - renewal in the past'))
            #renewal is set to a time in the past

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise validationError(_('Invalid date - renewal more than 4 weeks ahead'))
            #renewal has extended beyond the scope of th3 4 week renewal limit
            
        return data


