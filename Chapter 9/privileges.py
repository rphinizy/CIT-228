class Privileges:
        def __init__(self,privileges):
            self.privileges=privileges
        def show_privileges(self):
            print(f"User has the following permissions: ")
            print("***************************")
            for p in self.privileges:
                print(p.title())
            print("***************************")