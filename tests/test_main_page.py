import allure
import pytest

from data import Constants

@allure.title('Тесты на проверку вопросов и ответов')
@allure.description('Параметризованный тест')
class TestMainPage:

    @pytest.mark.parametrize(
        'number',
        [0, 1, 2, 3, 4, 5, 6, 7]
    )
    def test_questions_and_answers(self, main_page, number):
        main_page.click_to_question(number)
        assert main_page.get_answer_text(number) == Constants.ANSWERS[number]
