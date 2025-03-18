import os
import sys
import django
import pytest

# Add the project root to Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def pytest_configure():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')
    django.setup()

@pytest.fixture
def organizer():
    return Organizer.objects.create(name='Test Organizer', slug='test-organizer')

@pytest.fixture
def event(organizer):
    return Event.objects.create(
        organizer=organizer,
        name='Test Event',
        slug='test-event',
        date_from='2024-01-01',
        plugins='pretix_emailChecker'
    )