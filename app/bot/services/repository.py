from typing import Iterable, List
from app.bot.models.roles import User_role



class Repo:
  """
  db abstraction layer
  """
  
  def __init__(self, conn):
    self.conn = conn

  async def get_user(self, user_id) -> User_orm:
    ...
  
  async def get_users(self, user_ids: Iterable[int | str]) -> List[User_orm]:
    ...
