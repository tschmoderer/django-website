from django import forms
from django.template.loader import get_template

class MarkdownWidget(forms.widgets.Textarea):

    def render(self, name, value, attrs=None, renderer=None, **kwargs): 
        template = get_template('MDeditor/editor.html')
        widget   = super(MarkdownWidget, self).render(name, value, attrs={'hidden': '', 'id': attrs['id'], 'class': 'MDeditor'})
        
        return template.render({
            'field_name': name,
            'field_id':   attrs['id'], 
            'field':      widget, 
        })

    class Media:
        css = {
            'all': (
                'MDeditor/css/mdeditor.css',
            )
        }
    
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.11/ace.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.11/mode-markdown.min.js',
            'MDeditor/js/emoji.js',
            'MDeditor/js/emoji-picker.js',
            'MDeditor/js/mdeditor.js',
        )