# https://quera.org/problemset/21206
# ----------------------------------

from datetime import datetime
from typing import Optional

from models import Product, User


class Store:
    def __init__(self) -> None:
        self.products: dict[Product, int] = dict()
        self.users: list[User] = list()

    def add_product(self, product: Product, amount: int = 1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product: Product, amount: int = 1):
        inventory = self.products.get(product, 0)
        if inventory < amount:
            raise Exception("Not Enough Products")

        if inventory == amount:
            self.products.pop(product)
        else:
            self.products[product] -= amount

    def add_user(self, username: str) -> Optional[str]:
        user = User(username=username)
        if user in self.users:
            return None

        self.users.append(user)
        return username

    def get_total_asset(self) -> int:
        return sum(product.price * amount for product, amount in self.products.items())

    def get_total_profit(self) -> int:
        profit: int = 0
        for user in self.users:
            for product in user.bought_products:
                profit += product.price

        return profit

    def get_comments_by_user(self, user: User) -> list[str]:
        user_comments: list[str] = []
        for product in self.products:
            for comment in product.comments:
                if comment.user == user:
                    user_comments.append(comment.text)

        return user_comments

    def get_inflation_affected_product_names(self) -> list[str]:
        inflated_products: set[str] = set()
        seen_products: dict[str, int] = {}  # product-name: product-price
        for product in self.products:
            if product.name not in seen_products:
                seen_products[product.name] = product.price
            else:
                if seen_products[product.name] != product.price:
                    inflated_products.add(product.name)

        return list(inflated_products)

    def clean_old_comments(self, date: datetime):
        for product in self.products:
            product.comments = [
                comment for comment in product.comments if comment.date_added >= date
            ]

    def get_comments_by_bought_users(self, product: Product) -> list[str]:
        buyer_comments: list[str] = []

        for comment in product.comments:
            if product in comment.user.bought_products:
                buyer_comments.append(comment.text)

        return buyer_comments
