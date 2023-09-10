
class UserTypePermissionMixin:
    def is_admin(self, user):
        """
        Check if the user is an admin.
        """
        return user.user_type == 'admin'

    def is_vendor(self, user):
        """
        Check if the user is a vendor.
        """
        return user.user_type == 'vendor'

    def is_customer(self, user):
        """
        Check if the user is a customer.
        """
        return user.user_type == 'customer'

    def has_permission(self, user):
        """
        Check if the user has permission based on their user type.
        """
        # Example: Allow vendors and admins to perform an action
        return self.is_vendor(user) or self.is_admin(user)
