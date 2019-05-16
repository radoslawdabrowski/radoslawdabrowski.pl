from django import template
from django.utils.translation import ugettext as _

from cv.views import education_view_context, experience_view_context, interests_view_context, skills_view_context
from cv.views import skill_view_context, school_view_context, hobby_view_context, job_view_context

register = template.Library()


@register.inclusion_tag('components/cv/education.html')
def education():
    return education_view_context()


@register.inclusion_tag('components/cv/experience.html')
def experience():
    return experience_view_context()


@register.inclusion_tag('components/cv/interests.html')
def interests():
    return interests_view_context()


@register.inclusion_tag('components/cv/skills.html')
def skills():
    return skills_view_context()


@register.inclusion_tag('components/cv/single/school.html')
def school(item, wow=0.2):
    return school_view_context(item, wow)


@register.inclusion_tag('components/cv/single/job.html')
def job(item, wow=0.2):
    return job_view_context(item, wow)


@register.inclusion_tag('components/cv/single/hobby.html')
def hobby(item):
    return hobby_view_context(item)


@register.inclusion_tag('components/cv/single/skill.html')
def skill(item, wow=0.2):
    return skill_view_context(item, wow)