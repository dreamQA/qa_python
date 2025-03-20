import pytest
from main import BooksCollector


class TestBooksCollector:
    # Тестирование добавления новой книги
    @pytest.mark.parametrize("book_name, expected_genre", [
        ("Book 1", ""),
        ("Book 2", ""),
    ])
    def test_add_new_book(self,book_name, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre
        assert collector.books_genre[book_name] == expected_genre

        # Тестирование добавления книги с названием, превышающим 40 символов
    def test_add_new_book_exceeding_lenght(self):
        collector = BooksCollector()
        collector.add_new_book("B" * 41)
        assert "B" * 41 not in collector.books_genre

    @pytest.mark.parametrize("book_name", [
        "Book 1",
        "Book 2",
    ])
    # Тестирвоание добавления дубликата книги
    def test_add_duplicate_book(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_new_book(book_name) # Не должно сработать
        assert len(collector.books_genre) == 1

    # Тестирование выбора жанра для книги
    @pytest.mark.parametrize("book_name, genre", [
        ("Book 1","Фантастика"),
        ("Book 2", "Комедии"),
    ])
    def test_set_book_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # Тестирование установки не существующего жанра книги
    @pytest.mark.parametrize("book_name", [
    "Book 1",
    ])
    def test_set_book_genre_invalid(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, "Неизвестный жанр")
        assert collector.get_book_genre(book_name) == ""

    # Тестирование получения списка книг с определенным жанром
    @pytest.mark.parametrize("genre, expected_books",[
    ("Фантастика", ["Book 1", "Book 2"]),
    ])
    def test_get_books_with_specific_genre(self, genre, expected_books):
        collector = BooksCollector()
        for book_name in expected_books:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)
            #Добавляем 3-ю книгу с другим жанром
        collector.add_new_book("Book 3")
        collector.set_book_genre("Book 3", "Ужасы")

        books = collector.get_books_with_specific_genre(genre)
        for book in expected_books:
            assert book in books

    #Тестирование получения списка книг для детей
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Book 1")
        collector.set_book_genre("Book 1","Фантастика")
        collector.add_new_book("Book 2")
        collector.set_book_genre("Book 2","Ужасы")

        children_books = collector.get_books_for_children()
        assert "Book 1" in children_books
        assert "Book 2" not in children_books

    #Тестирование добавления книги в избранное
    @pytest.mark.parametrize("book_name",[
        "Book 1",
        "Book 2",
    ])
    def test_add_book_in_favorites(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites

    @pytest.mark.parametrize("book_name", [
        "Book 1",
        "Book 2",
    ])
    def test_add_duplicate_book_in_favorites(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.favorites) == 1

    #Тестирование удаления книги из избранного
@pytest.mark.parametrize("book_name", [
        "Book 1",
        "Book 2",
    ])
def test_delete_book_from_favorites(book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    collector.delete_book_from_favorites(book_name)
    assert book_name not in collector.favorites

# Тестирование получения списка избранных книг
@pytest.mark.parametrize("book_name", [
    "Book 1",
])
def test_get_list_of_favorites_books(book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    favorites = collector.get_list_of_favorites_books()
    assert favorites == [book_name]


def test_add_new_book_add_two_books():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    assert len(collector.books_genre) == 2


#Запуск тестов
if __name__ == "__main__":
    pytest.main()