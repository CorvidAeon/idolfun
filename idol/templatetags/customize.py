from django import template
#fix this to import some location vars from elsewhere
    # spread_save_loc = "idol/static/images/spread/"
    # puchi_save_loc = "idol/static/images/puchi/"
    # icon_save_loc = "idol/static/images/icon/"
register = template.Library()
@register.filter 
def create_spread_uri(id):
    return "images/spread/"+str(id)+".png"

@register.filter 
def create_puchi_uri(id):
    return "images/puchi/"+str(id)+".png"

@register.filter 
def create_icon_uri(id):
    return "images/icon/"+str(id)+".png"

@register.filter
def list_access(list, index):
    return list[index]