from django import template

register = template.Library()

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    hlen = len(hex)
    return tuple(int(hex[i:i+hlen/3], 16) for i in range(0, hlen, hlen/3))


register.filter('hex_to_rgb', hex_to_rgb)