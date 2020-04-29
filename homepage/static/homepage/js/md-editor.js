$(function() {
    /* enable tooltip in the toolbar */
    $('[data-toggle="tooltip"]').tooltip()
});

//$("#emoji-people-tab").html(twemoji(emojis["people"][0]));

$('#editor-list a').on('click', function(e) {
    e.preventDefault()
    $(this).tab('show')
})

$('#editor-tab').click(function() {
    editor.focus();
});

$('#preview-tab').click(function() {
    $('#btn-smile').popover('hide');
});

editor.setOptions({
    mode: "ace/mode/markdown",
    maxLines: 30,
    minLines: 30,
    autoScrollEditorIntoView: true,
});

editor.setFontSize("14px");
editor.session.setUseWrapMode(true);

editor.getSession().setValue(textarea.val());
preview.html(md.render(editor.getSession().getValue()));

editor.focus();

editor.getSession().on('change', function() {
    var dirty = md.render(editor.getSession().getValue());
    var config = {
        ADD_TAGS: ['iframe'],
        SAFE_FOR_JQUERY: true
    };
    var clean = DOMPurify.sanitize(dirty, config);
    preview.html(clean);
    MathJax.typeset()
});


$(document).ready(function() {
    $('#btn-smile').popover({
        html: true,
        title: ' ',
        position: 'bottom',
        content: $('#emoji-popover-content').html(),
    })
});


$('#btn-smile').on('shown.bs.popover', function() {
    $('.popover-body').emojiPickerContainer({
        twemoji: true,
        width: 235,
        closeOnSelect: false,
        onSelect: function(emoji) {
            editor.insert(':' + emoji.name + ':');
        }
    });
});
// on submit set textarea value
$('#homepage-form').submit(function() {
    textarea.val(editor.getSession().getValue());
});


$('#btn-bold').click(function() {
    editor.insert("**text**");
    editor.find('text', {
        backwards: true,
        caseSensitive: true,
        wholeWord: true,
    });
    editor.focus();
});

$('#btn-italic').click(function() {
    editor.insert("*text*");
    editor.find('text', {
        backwards: true,
        caseSensitive: true,
        wholeWord: true,
    });
    editor.focus();
});

$('#btn-underline').click(function() {
    editor.insert("__text__");
    editor.find('text', {
        backwards: true,
        caseSensitive: true,
        wholeWord: true,
    });
    editor.focus();
});

$('#btn-strike').click(function() {
    editor.insert("~~text~~");
    editor.find('text', {
        backwards: true,
        caseSensitive: true,
        wholeWord: true,
    });
    editor.focus();
});

$('#btn-header').click(function() {
    editor.insert("#");
    editor.focus();
});

$('#btn-line').click(function() {
    editor.insert("\n***\n");
    editor.focus();
});

$('#btn-list').click(function() {
    editor.insert("\t* ");
    editor.focus();
});

$('#btn-num-list').click(function() {
    editor.insert("\t1. ");
    editor.focus();
});

$('#btn-table').click(function() {
    editor.insert("| Column 1 | Column 2 | Column 3 |\n| -------- |:-------------:| -----:|\n| col 1 is | right-aligned | $1600 |\n| col 2 is | centered      |   $12 |\n| col 3 is | left-aligned  |    $1 |\n ");

    editor.find('Column 1', {
        backwards: true,
        caseSensitive: true,
        wholeWord: true,
    });
});

$('#btn-math').click(function() {
    editor.insert("$$\nmath\n$$\n");
    editor.find('math', {
        backwards: true,
        caseSensitive: true,
        wholeWord: true,
    });
    editor.focus();
});

$('#btn-code').click(function() {
    editor.insert("```\ncode\n```");
    editor.find('code', {
        backwards: true,
        caseSensitive: true,
        wholeWord: true,
    });
    editor.focus();
});

$('#btn-quote').click(function() {
    editor.insert("> ");
    editor.focus();
});

$('#btn-link').click(function() {
    editor.insert("[link](https://www.)");
    editor.find('link', {
        backwards: true,
        caseSensitive: true,
        wholeWord: true,
    });
});

$('#btn-image').click(function() {
    editor.insert("![image](src)");
    editor.find('image', {
        backwards: true,
        caseSensitive: true,
        wholeWord: true,
    });
});

$('#btn-undo').click(function() {
    editor.undo();
});

$('#btn-redo').click(function() {
    editor.redo();
});