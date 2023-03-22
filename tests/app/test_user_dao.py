import unittest

from app.dao.user_dao import UserDao


class TestUserService(unittest.TestCase):

    def test_where_statements_generator(self):
        dao = UserDao()

        where_statement, params = dao.build_statement_parts({"id": 1, "rating_gte": 1, "primary_skills": ["slow"]})
        expected_where_statement = "id = (?) AND rating >= (?) AND primary_skills LIKE '%' || (?) || '%'"

        assert where_statement == expected_where_statement
        assert params == [1, 1, "slow"]
