from uuid import uuid4

categories = {}

class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.id = uuid4()

class Category_Service:
    def create(self, category_obj: Category):
        """
        Creates a new category and adds it to the categories dictionary.

        Parameters:
        - category_obj (Category): The Category object to be created.
        """
        categories[str(category_obj.id)] = {
            "name": category_obj.name,
            "description": category_obj.description
        }
        print(f"{category_obj.name} has been created")
        print(categories)

    def update(self, id, name, description):
        """
        Updates an existing category in the categories dictionary.

        Parameters:
        - id (str): The ID of the category to be updated.
        - name (str): The new name for the category.
        - description (str): The new description for the category.
        """
        current_category = self.get_by_id(id)
        if current_category:
            current_category.update({
                "name": name,
                "description": description
            })
            print(f"{id} category has been updated")
        else:
            print(f"Category with ID {id} not found")

    def delete(self, id):
        """
        Deletes a category from the categories dictionary.

        Parameters:
        - id (str): The ID of the category to be deleted.
        """
        current_category = self.get_by_id(id)
        if current_category:
            del categories[id]
            print(f"Category with ID {id} has been deleted")
        else:
            print(f"Category with ID {id} not found")

    def get_all(self):
        """ Prints all categories in the categories dictionary. """
        print(categories)

    def get_by_id(self, id) -> dict:
        """
        Retrieves a category from the categories dictionary by its ID.

        Parameters:
        - id (str): The ID of the category to retrieve.

        Returns:
        - dict: The category information as a dictionary.
        """
        return categories.get(id, {})


def main():
    """
    Main function to interact with Category_Service through command-line interface.
    """
    while True:
        service = Category_Service()
        process = input("Please type an action: \n"
                        "create / get all / get by id / update / delete / exit \n").lower()

        if process == "exit":
            print("App is closing")
            break
        elif process == "create":
            name = input("Name: ")
            desc = input("Description: ")
            category_obj = Category(name, desc)
            service.create(category_obj)
            service.get_all()
        elif process == "get all":
            service.get_all()
        elif process == "get by id":
            id = input("Enter ID: ")
            category = service.get_by_id(id)
            if category:
                print(category)
            else:
                print(f"Category with ID {id} not found")
        elif process == "update":
            id = input("Enter ID: ")
            name = input("New Name: ")
            desc = input("New Description: ")
            service.update(id, name, desc)
        elif process == "delete":
            id = input("Enter ID: ")
            service.delete(id)
        else:
            print("Please type a correct transaction name.")

if __name__ == "__main__":
    main()
