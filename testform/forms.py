from django import forms
#add form data to models
from testform.models import model_testform
from django.views.generic.edit import UpdateView
from django.core import validators

class form_testform(forms.ModelForm):
    parkSpecialLane = forms.ChoiceField(label='Parking Lane or Other Special Lane',choices=[("", ""),("N", "N"),("PK", "PK"),("SP", "SP"),("CLP", "CLP"),("BL", "BL"),("OTH", "OTH")])
    blockID = forms.CharField(label='Block ID', required = True)
    consistantBlock = forms.BooleanField(label='Consistant Block', required = False)
    rodwayType = forms.ChoiceField(required = False, label='Roadway Type',choices=[("", ""),("2U", "2U"),("3T", "3T"),("4U", "4U"),("4D", "4D"),("5T", "5T"),("6U", "6U"),("6D", "6D")])
    medianType = forms.ChoiceField(required = False, label='Median Type',choices=[("", ""),("N", "N"),("R", "R"),("D", "D"),("F", "F")])
    horAlignment = forms.ChoiceField(required = False, label='Horizontal Alignment',choices=[("", ""),("T", "T"),("GC", "GC"),("SC", "SC")])
    speedLimit = forms.ChoiceField(required = False, label='Speed Limit', choices=[(x, x) for x in range(0, 70, 5)])
    shoulderChoices = [("",""),("P",'P'),("T",'T'),("G",'G'),("C",'C'),("VC",'VC'),("MC",'MC'),("CG",'CG'),("MG",'MG'),("PC",'PC'),("N",'N')];
    shoulderTypeDec = forms.ChoiceField(required = False, label='Shoulder Type',choices=shoulderChoices)
    shoulderWidthDec = forms.IntegerField(required = False, label='Shoulder Width')
    gutterWidthDec = forms.IntegerField(required = False, label='Gutter Width')
    rightLWidthDec = forms.IntegerField(required = False, label='Right Lane Width')
    centerLWidthDec = forms.IntegerField(required = False, label='Center Lane Width')
    LeftLWidthDec = forms.IntegerField(required = False, label='Left Lane Width')
    shoulderTypeInc = forms.ChoiceField(required = False, label='Shoulder Type',choices=shoulderChoices)
    shoulderWidthInc = forms.IntegerField(required = False, label='Shoulder Width')
    gutterWidthInc = forms.IntegerField(required = False, label='Gutter Width')
    rightLWidthInc = forms.IntegerField(required = False, label='Right Lane Width')
    centerLWidthInc = forms.IntegerField(required = False, label='Center Lane Width')
    LeftLWidthInc = forms.IntegerField(required = False, label='Left Lane Width')
    comment = forms.CharField(required = False, label='Comments', widget=forms.Textarea)
    stateList=[("",""),("AL",'AL'),("AK",'AK'),("AZ",'AZ'),("AR",'AR'),("CA",'CA'),("CO",'CO'),("CT",'CT'),("DE",'DE'),("FL",'FL'),("GA",'GA'),("HI",'HI'),("ID",'ID'),("IL",'IL'),("IN",'IN'),("IA",'IA'),("KS",'KS'),("KY",'KY'),("LA",'LA'),("ME",'ME'),("MD",'MD'),("MA",'MA'),("MI",'MI'),("MN",'MN'),("MS",'MS'),("MO",'MO'),("MT",'MT'),("NE",'NE'),("NV",'NV'),("NH",'NH'),("NJ",'NJ'),("NM",'NM'),("NY",'NY'),("NC",'NC'),("ND",'ND'),("OH",'OH'),("OK",'OK'),("OR",'OR'),("PA",'PA'),("RI",'RI'),("SC",'SC'),("SD",'SD'),("TN",'TN'),("TX",'TX'),("UT",'UT'),("VT",'VT'),("VA",'VA'),("WA",'WA'),("WV",'WV'),("WI",'WI'),("WY",'WY')]
    state = forms.ChoiceField(required = False, label='State',choices=stateList)

    def clean_shoulderWidthDec(self):
        data = self.cleaned_data['shoulderWidthDec']
        print (data)
        if data == None:
            data = 1
        if data>50 or data<1:
            raise forms.ValidationError("Shoulder width out of range")
        return self.cleaned_data['shoulderWidthDec']

    class Meta:
        model = model_testform
        fields = '__all__'
