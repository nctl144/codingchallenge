from app.dao.base_dao import BaseDao

class UserDao(BaseDao):
    def __init__(self):
        super().__init__()

    
    def insert_users(self, users):
        params = [(user.id, 
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
                    0) for user in users]
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
            self.cursor.executemany(sql, params)
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
        
    def search_users(self, filters):
        where_statement, params = self.build_statement_parts(filters)
        
        sql = f"""
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
        WHERE {where_statement}
        """

        print(sql)

        return self.cursor.execute(sql, params).fetchall()
        
    def build_statement_parts(self, filters):
        params = []
        where_statement = ""
        where_statement_parts = []
    
        for attr in filters.keys():
            if attr == "rating_gte":
                where_statement_parts.append("rating >= (?)")
                params.append(filters.get("rating_gte"))
            elif attr == "rating_lte":
                where_statement_parts.append("rating <= (?)")
                params.append(filters.get("rating_lte"))
            elif attr in ("primary_skills", "secondary_skill"):
                for skill in filters.get(attr):
                    where_statement_parts.append(f"{attr} LIKE '%' || (?) || '%'")
                    params.append(skill)
            else:
                where_statement_parts.append(f"{attr} = (?)")
                params.append(filters.get(attr))
        
        if len(where_statement_parts) > 1:
            where_statement += " AND ".join(where_statement_parts)
        else:
            where_statement += "".join(where_statement_parts)
        
        return where_statement, params
    
    def update_searched_user_count(self, users):
        user_ids = [tuple([user[0]]) for user in users]

        sql = """
        UPDATE tblUsers
        SET search_count = search_count + 1
        WHERE id = (?)
        """
        self.cursor.executemany(sql, user_ids)
        self.conn.commit()

    def get_most_popular_users(self):
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
        ORDER BY search_count DESC
        """
        return self.cursor.execute(sql).fetchall()
    
    def get_least_popular_users(self):
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
        ORDER BY search_count ASC
        """
        return self.cursor.execute(sql).fetchall()
    