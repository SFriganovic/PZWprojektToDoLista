from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import CustomLoginView, RegisterPage, TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('homepage')
        # print(resolve(url))

        self.assertEquals(resolve(url).func, homepage)

    def test_books_url_is_resolved(self):
        url = reverse('books')

        self.assertEquals(resolve(url).func.view_class, BookList)

    def test_authors_url_is_resolved(self):
        url = reverse('authors')

        self.assertEquals(resolve(url).func.view_class, AuthorList)

    def test_authors_url_is_resolved(self):
        url = reverse('author_q', args=['some-author'])

        self.assertEquals(resolve(url).func.view_class, AuthorBookList)