import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """Was published recently returns false for questions whose
            pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quien es el mejor CD de platzi?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
    
    def test_was_published_recently_with_past_questions(self):
        """Was published recently returns false for questions whose pub_date is in the past"""
        time = timezone.now() - datetime.timedelta(days=30)
        past_question = Question(question_text="¿Quien es el mejor CD de platzi?", pub_date=time)
        self.assertIs(past_question.was_published_recently(), False)
    
    def test_was_published_recently_with_present_questions(self):
        """Was published recently returns false for questions whose pub_date is in the present"""
        time = timezone.now()
        present_question = Question(question_text="¿Quien es el mejor CD de platzi?", pub_date=time)
        self.assertIs(present_question.was_published_recently, True)



