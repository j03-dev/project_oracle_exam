from repositories.article_repository import ArticleRepository
from repositories.category_repository import CategoryRepository
from repositories.image_repository import ImageRepository
from repositories.user_repository import UserRepository

repositories = [UserRepository(), ImageRepository(), ArticleRepository(), CategoryRepository()]


def migrate():
    for repo in repositories:
        repo.migration()


if __name__ == "__main__":
    migrate()
