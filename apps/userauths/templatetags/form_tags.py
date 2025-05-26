from django import template

register = template.Library()

@register.filter
def add_input_class(field):
    """Adds Bootstrap 'form-control' and optionally 'is-invalid' to input fields."""
    classes = "form-control"
    if field.errors:
        classes += " is-invalid"
    return field.as_widget(attrs={"class": classes})
