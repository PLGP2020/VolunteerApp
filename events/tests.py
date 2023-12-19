from django.test import TestCase

from events.models import Event 


class EventModelTest(TestCase):

    def test_saving_events(self):

        first_event = Event()
        first_event.title = 'First event title'
        first_event.save()

        second_event = Event()
        second_event.title = 'Second event title'
        second_event.save()

        saved_events = Event.objects.all()
        self.assertEqual(saved_events.count(), 2)

        first_event = saved_events[0]
        second_event = saved_events[1]

        self.assertEqual(first_event.title, 'First event title')
        self.assertEqual(second_event.title, 'Second event title')  

         


