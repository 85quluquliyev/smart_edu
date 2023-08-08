from django.shortcuts import get_object_or_404, render
from . models import Course, Category, Tag

"""def course_list(request):
    courses = Course.objects.all().order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags':tags,
    }

    return render(request, 'courses.html', context) """

def course_list(request, category_slug = None, tags_slug = None):
        category_page = None
        tag_page = None
        categories = Category.objects.all()
        tags = Tag.objects.all()

        if category_slug != None:
            category_page = get_object_or_404(Category, slug = category_slug)
            courses = Course.objects.filter(available=True, category=category_page)

        elif tags_slug != None:
             tag_page = get_object_or_404(Tag, slug = tags_slug)
             courses = Course.objects.filter(available=True, tags = tag_page)

        else:
            courses = Course.objects.all().order_by('-date')
        
        context = {
            'courses': courses,
            'categories': categories,
            'tags':tags,
        }

        return render(request, 'courses.html', context)




def course_detail(request, category_slug, course_id):
    
    course = Course.objects.get(category__slug=category_slug, id = course_id)
    
    context = {
        'course': course
    }

    return render(request, 'course.html', context)


def search(request):
    courses = Course.objects.filter(name__contains = request.GET['search'])
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'courses': courses,
        'categories': categories,
        'tags':tags,
    }

    return render(request, 'courses.html', context)







"""def category_list(request, category_slug):
    
    courses = Course.objects.all().filter(category__slug = category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags':tags,
    }

    return render(request, 'courses.html', context)"""

"""def tags_list(request, tags_slug):

    courses = Course.objects.all().filter(tags__slug = tags_slug)
    tags = Tag.objects.all()
    categories = Category.objects.all()

    context = {
        'courses':courses,
        'tags':tags,
        'categories': categories
    }

    return render(request, 'courses.html', context)"""
