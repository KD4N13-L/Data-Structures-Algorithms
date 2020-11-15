class Bowl:
    bowl_count = 0

    def __init__(self, material_dict, shape_dict, volume_dict, appearance_dict, contents_list, maker_dict):
        self.material_dict = {
            "name": "substance_name", "density": {
                "unit": "measurement_name", "value": "density value"
            }
        }
        self.shape_dict = {
            "length_unit": "length_unit", "measurements": {
                "height": "0", "max_outer_diam": "0", "max_inner_diam": "0", "stand_diam": "0", "depth": "0",
                "thickness": "0"
            }
        }
        self.volume_dict = {
            "volume_unit": "volume_unit", "volume": "0"
        }
        self.appearance_dict = {
            "material_pattern": "material_pattern", "color_pattern": "color_pattern", "color_s": []
        }
        self.contents_list = []
        self.maker_dict = {
            "name": "name", "organization_type": "organization_type", "location": "location"
        }
        Bowl.bowl_count = Bowl.bowl_count + 1

    def display_contents(self):
        print("Items currently stored in your bowl:")
        for x in self.contents_list:
            i = self.contents_list.index(x)
            a = x["name"]
            b = x["consumability"]
            print("Name:", a, "| Consumability:", b, "| Item Index:", i)
        print("------------------------------------------------------------------------------------------------")

    def store(self, to_be_added_item):
        self.contents_list.append(to_be_added_item)
        print(to_be_added_item["name"], "has been stored in the bowl.")
        print("------------------------------------------------------------------------------------------------")

    def clear_storage(self):
        self.contents_list.clear()
        print("Bowl cleared.")
        print("------------------------------------------------------------------------------------------------")

    def remove_item(self):
        self.display_contents()
        to_be_removed_list_index = int(input("Which item would you like to remove? Insert its INDEX: "))
        print("------------------------------------------------------------------------------------------------")
        self.contents_list.pop(to_be_removed_list_index)
        print("Updated list of items in your bowl:")
        for x in self.contents_list:
            i = self.contents_list.index(x)
            a = x["name"]
            b = x["consumability"]
            print("Name:", a, "| Consumability:", b, "| Item Index:", i)
        print("------------------------------------------------------------------------------------------------")

    def consume(self):
        for i in self.contents_list:
            if not i["consumability"]:
                print(i["name"], "is nonconsumable")
                print("Cannot proceed to consuming the contents. Please, remove all nonconsumables and try again.")
                print(
                    "------------------------------------------------------------------------------------------------")
                break
            else:
                print(i["name"], "is consumable.")
                print(
                    "------------------------------------------------------------------------------------------------")
                print(i["name"], "consumed. Yum. Yum.")
                print(
                    "------------------------------------------------------------------------------------------------")


# Additional Ideas for Methods:
# 1. Draw circles with
# 2. Plug a circular hole
# 3. Cover a tiny creature (ex: insect, mouse)
# 4. Cover a light source (either completely or partially)
# 5. Put a phone inside as a holder
# 6. Calculate volume (if the function which defines the curve of the walls is given)
# 7. Calculate mass (using density and the calculated volume)
