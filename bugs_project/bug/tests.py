from django.test import TestCase
from .models import Bug
from django.urls import reverse


class BugModelTestCase(TestCase):
    """tests the models for any bugs"""

    def test_default_report_date(self):
        """Test if the default value of report_date is now"""
        bug = Bug.objects.create(
            description="Test bug description",
            bug_type="error",
            status="todo"
        )
        self.assertIsNotNone(bug.report_date)

    def test_create_bug(self):
        """tests whether a bug is being added the database"""
        bug = Bug.objects.create(
            description="Test bug description",
            bug_type="error",
            status="todo"
        )
        self.assertIsNotNone(bug)

    def test_bug_type(self):
        """tests whether a bug is being added the database"""
        bug = Bug.objects.create(
            description="Test bug description",
            bug_type="error",
            status="todo"
        )
        self.assertIsNotNone(bug.bug_type)

    def test_description(self):
        """tests whether a bug is being added the database"""
        bug = Bug.objects.create(
            description="Test bug description",
            bug_type="error",
            status="todo"
        )
        self.assertIsNotNone(bug.description)


class BugViewTestCase(TestCase):
    """tests the view.py for any errors"""

    def setUp(self):
        """Create sample bug instances for testing"""
        self.bug1 = Bug.objects.create(
            description="Bug 1 description",
            bug_type="error",
            status="todo"
        )
        self.bug2 = Bug.objects.create(
            description="Bug 2 description",
            bug_type="feature",
            status="in_progress"
        )

    def test_bug_list_view(self):
        """Test if the bug list view returns a 200 status code"""
        response = self.client.get(reverse('bug-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.bug1.description)
        self.assertContains(response, self.bug2.description)

    def test_bug_details_view(self):
        """Test if the bug details view returns a 200 status code"""
        b = 'bug-details'
        response = self.client.get(reverse(b, args=(self.bug1.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.bug1.description)
        self.assertNotContains(response, self.bug2.description)

    def test_bug_list_view_empty(self):
        """Test the bug list view when there are no bugs"""
        Bug.objects.all().delete()  # Delete all bugs
        response = self.client.get(reverse('bug-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "")
