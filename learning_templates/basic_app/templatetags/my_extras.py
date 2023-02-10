from django import template

register = template.Library()

@register.filter(name='cut_a_string')  #this is a decorator
def cut_a_string(value,arg):
    """
    This cuts our all values of "arg" from the string!
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg,'')


# register.filter('cut',cut)   #first argument is what I want to call the filter, the second is the function itself


