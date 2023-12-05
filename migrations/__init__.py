from repositories.admin_repository import AdminRepository
from repositories.category_repository import CategoryRepository
from repositories.product_repository import ProductRepository

repositories = [AdminRepository(), CategoryRepository(), ProductRepository()]


def migrate():

    for repo in repositories:
        repo.migration()


def drop():
    for repo in repositories[::-1]:
        try:
            repo.drop()
        except:
            pass


if __name__ == "__main__":
    migrate()
