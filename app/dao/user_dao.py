from app.dao.base_dao import BaseDao

class UserDao(BaseDao):
    def __init__(self):
        super().__init__()

    
    def insert_user(self, user):
        sql = """
        INSERT INTO tblUsers (
            id,
            first_name,
            last_name,
            sex,
            birth_date,
            rating,
            primary_skills,
            secondary_skill,
            company,
            active,
            country,
            language,
            search_count
        ) VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
        """
        try:
            self.cursor.execute(
                sql, 
                (
                    user.id, 
                    user.first_name, 
                    user.last_name, 
                    user.sex, 
                    user.birth_date, 
                    user.rating, 
                    user.primary_skills, 
                    user.secondary_skills, 
                    user.company, 
                    user.active, 
                    user.country, 
                    user.language,
                    0
                )
            )
            self.conn.commit()
        except Exception as e: 
            raise Exception("Failed to insert user, check request", e)

    def retrieve_user_with_id(self, id):

        sql = """
        SELECT 
            id,
            first_name,
            last_name,
            sex,
            birth_date,
            rating,
            primary_skills,
            secondary_skill,
            company,
            active,
            country,
            language,
            search_count
        FROM tblUsers
        """ 

        return self.cursor.execute(sql).fetchone()
        