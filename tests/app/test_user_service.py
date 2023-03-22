import unittest

from app.services.user_service import UserService


class TestUserService(unittest.TestCase):

    def test_validate_filters_failed(self):
        service = UserService()
        with self.assertRaises(Exception):

            result = service.validate_user_filters({"delete": 1})

    def test_validate_filters(self):
        service = UserService()

        result = service.validate_user_filters({"id": 1})
        assert result == None
