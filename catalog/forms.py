from django import forms

from catalog.models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'image']

    FORBIDDEN_WORDS = [
        'казино',
        'криптовалюта',
        'крипта',
        'биржа',
        'дешево',
        'бесплатно',
        'обман',
        'полиция',
        'радар'
    ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Название продукта'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Цена продукта'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'type': "text", 'placeholder': 'Описание продукта', 'rows': 5})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})

    def clean_price(self):
        praice = self.cleaned_data.get('price')
        if praice < 0:
            raise forms.ValidationError('Цена не может быть отрицательной')
        return praice

    def clean_name(self):
        name = self.cleaned_data.get('name')
        name_lower = name.lower()
        for word in self.FORBIDDEN_WORDS:
            if word in name_lower:
                raise forms.ValidationError(
                    f'В поле "{'Наименование'}" нельзя использовать слово "{word}"'
                )
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        description_lower = description.lower()
        for word in self.FORBIDDEN_WORDS:
            if word in description_lower:
                raise forms.ValidationError(
                    f'В поле "{'Описание'}" нельзя использовать слово "{word}"'
                )
        return description


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Название категории'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'type': "text", 'placeholder': 'Описание категории', 'rows': 5})
