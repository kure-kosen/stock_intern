from django.test import TestCase
from django.urls import reverse
from articles.models import Article, Category
from accounts.models import User


class ArticleModelTests(TestCase):
    user_id = 'chanyou0311'
    user_name = 'ちゃんゆー'
    password = 'hogehoge'
    category_name = '長期インターンシップ'
    text = "親譲りの無鉄砲で小供の時から損ばかりしている。小学校に居る時分学校の二階から飛び降りて一週間ほど腰を抜かした事がある。" \
           "なぜそんな無闇をしたと聞く人があるかも知れぬ。別段深い理由でもない。"

    def create_user(self):
        user = User(user_id=self.user_id, user_name=self.user_name, password=self.password)
        user.save()

    def create_category(self):
        category = Category(category_name=self.category_name)
        category.save()

    def test_category_model_ok(self):
        category = Category(category_name=self.category_name)
        category.save()

        category_instance = Category.objects.get(id=1)
        self.assertEqual(self.category_name, category_instance.category_name)

    def test_article_model_ok(self):
        self.create_user()
        self.create_category()
        user_instance = User.objects.get(user_id=self.user_id)
        category_instance = Category.objects.get(id=1)
        article = Article(text=self.text, user_id=user_instance, category_id=category_instance)
        article.save()

        article_instance = Article.objects.get(id=1)
        self.assertEqual(self.text, article_instance.text)


class ArticleViewTests(TestCase):
    def test_index_ok(self):
        response = self.client.get(reverse('articles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')
