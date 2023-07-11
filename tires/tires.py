from abc import ABC


class Tires(ABC):
    def needs_service(self):
        """
        Checks if a set of tires needs servicing.

        This method should be implemented by concrete tires classes.
        It should perform checks to determine if the tires requires any maintenance or service.
        The specific implementation will depend on the type of tires being used.

        Returns:
            bool: True if the tires needs service, False otherwise.
        """
        pass
    