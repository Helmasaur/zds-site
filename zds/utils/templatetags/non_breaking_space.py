from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter('non_breaking_space')
@stringfilter
def non_breaking_space(str):
    return mark_safe(
        # Narrow non-breaking space: &#8239;
		str.replace(' ;', '&#8239;;')
		   .replace(' ?', '&#8239;?')
		   .replace(' !', '&#8239;!')
		   .replace(' %', '&#8239;%')
        # Non-breaking space: &nbsp;
		   .replace('« ', '«&nbsp;')
		   .replace(' »', '&nbsp;»')
		   .replace(' :', '&nbsp;:')
	)