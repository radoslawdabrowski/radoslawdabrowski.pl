from django.shortcuts import render
from .models import EducationEntity, ExperienceEntity, InterestEntity, SkillCategoryDictionary
from attributes.models import AttributeEntity


def cv_view(request, *args, **kwargs):
    return render(request, 'cv.html', {})


def education_view_context():
    return {
        'educations': EducationEntity.objects.all().order_by('-start_date')
    }


def experience_view_context():
    return {
        'experiences': ExperienceEntity.objects.all().order_by('-start_date')
    }


def interests_view_context():
    return {
        'description': AttributeEntity.objects.filter(key='ATTRIBUTE_INTERESTS_DESCRIPTION').get(),
        'interests': InterestEntity.objects.all()
    }


def about_view_context():
    return {
        'welcome': AttributeEntity.objects.filter(key='ATTRIBUTE_WEBSITE_WELCOME').get()
    }


def skills_view_context():
    count = SkillCategoryDictionary.objects.count()
    if count is 0:
        count = 12

    columns = 12 / count

    categories = SkillCategoryDictionary.objects.all()
    dictionary = {}

    for category in categories:
        dictionary[category] = category.skill_set.all()

    return {
        "skills_category_count": count,
        "categories": dictionary,
        "columns": columns
    }
