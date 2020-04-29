from django import forms


class MarkdownWidget(forms.widgets):
    
    def render(self, name, value, attrs=None, renderer=None, **kwargs):
        # Make the settings the default attributes to pass
        attributes_to_pass = {
            'data-enable-configs': MARTOR_ENABLE_CONFIGS,
            'data-upload-url': MARTOR_UPLOAD_URL,
            'data-markdownfy-url': MARTOR_MARKDOWNIFY_URL,
            'data-search-users-url': MARTOR_SEARCH_USERS_URL,
            'data-base-emoji-url': MARTOR_MARKDOWN_BASE_EMOJI_URL
        }

        # Make sure that the martor value is in the class attr passed in
        if 'class' in attrs:
            attrs['class'] += ' martor'
        else:
            attrs['class'] = 'martor'

        # Update and overwrite with the attributes passed in
        attributes_to_pass.update(attrs)

        # Update and overwrite with any attributes that are on the widget
        # itself. This is also the only way we can push something in without
        # being part of the render chain.
        attributes_to_pass.update(self.attrs)

        widget = super(MartorWidget, self).render(name, value, attributes_to_pass)

        template = get_template('martor/editor.html')

        return template.render({
            'martor': widget,
            'field_name': name,
            'emoji_enabled': emoji_enabled,
            'mentions_enabled': mentions_enabled
        })

    class Media:
        css = {
            'all': (
                'css/emoji.css',
            )
        }
        js = (
            'js/emoji.js',
            'js/emoji-picker.js',
            'js/md-editor.js',
        )