from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

# Create your tests here.

from .models import Course, Step


class CourseModelTest(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title="A simple title",
            description="A simple description"
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)


class StepModelTesting(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="A really simple title",
            description="A really simple description"
        )

    def test_step_creation(self):
        step = Step.objects.create(
            title="A simple second title",
            description="A simple second description",
            course=self.course
        )
        self.assertIn(step, self.course.step_set.all())


class CourseViews(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="A really simple title",
            description="A really simple description"
        )
        self.course_two = Course.objects.create(
            title="A really simple title again",
            description="A really simple description again"
        )
        self.step = Step.objects.create(
            title="A really simple title",
            description="A really simple description",
            course=self.course
        )

    def test_course_list_view(self):
        response = self.client.get(reverse('courses:list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.course, response.context['courses'])
        self.assertIn(self.course_two, response.context['courses'])
        self.assertTemplateUsed(response, 'courses/course_list.html')
        self.assertContains(response, self.course.title)

    def test_course_detail_view(self):
        response = self.client.get(reverse('courses:detail', kwargs={'pk': self.course_two.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.course_two, response.context['course'])
        self.assertTemplateUsed(response, 'courses/course_detail.html')
        self.assertContains(response, self.course.title)

    def test_step_detail_view(self):
        response = self.client.get(reverse('courses:step', kwargs={'course_pk': self.course.pk,
                                                                   'step_pk': self.step.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.step, response.context['step'])
        self.assertTemplateUsed(response, 'courses/step_detail.html')
        self.assertContains(response, self.course.title)

