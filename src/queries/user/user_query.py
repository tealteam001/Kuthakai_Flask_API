from ...models.user.user import UserModel

class UserQuery(UserModel):

    def get_user_by_id(self, user_id):
        user = self.query.get_or_404(user_id)
        return user