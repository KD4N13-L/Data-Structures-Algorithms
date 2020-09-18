from object_bowl import *

bowl1_material = {"name": "plastic", "density": {"unit": "gram/cm^3", "value": 0.92}}

bowl1_shape = {"length_unit": "cm", "measurements": {"height": 6.3, "max_outer_diam": 13.3, "max_inner_diam": 12.5,
                                                     "stand_diam": 5.7, "depth": 6.3, "thickness": 0.2}}

bowl1_volume = {"volume_unit": "liter", "volume": 0.5}

bowl1_appearance = {"material_pattern": "horizontal stripes", "color_pattern": "none", "color_s": ["green"]}

item0 = {"name": "air", "consumability": True}
item1_1 = {"name": "screw", "consumability": False}
item1_2 = {"name": "cookies", "consumability": True}

bowl1_contents = [item0]

bowl1_maker = {"name": "unknown", "organization_type": "unknown", "location": "unknown"}

bowl1 = Bowl(bowl1_material, bowl1_shape, bowl1_volume, bowl1_appearance, bowl1_contents, bowl1_maker)


# ----------------------------------------------------------------------------------------------

bowl2_material = {"name": "ceramic", "density": {"unit": "gram/cm^3", "value": 3}}

bowl2_shape = {"length_unit": "cm", "measurements": {"height": 10.2, "max_outer_diam": 15.5, "max_inner_diam": 13.9,
                                                     "stand_diam": 7.2, "depth": 10, "thickness": 0.2}}

bowl2_volume = {"volume_unit": "liter", "volume": 1}

bowl2_appearance = {"material_pattern": "smooth", "color_pattern": "horizontal stripes", "color_s": ["red", "yellow", "blue", "purple"]}

item0 = {"name": "air", "consumability": True}
item2_1 = {"name": "pickles", "consumability": True}
item2_2 = {"name": "pencil", "consumability": False}

bowl2_contents = [item0]

bowl2_maker = {"name": "unknown", "organization_type": "unknown", "location": "unknown"}

bowl2 = Bowl(bowl2_material, bowl2_shape, bowl2_volume, bowl2_appearance, bowl2_contents, bowl2_maker)

# ----------------------------------------------------------------------------------------------

bowl1.store(item0)

Bowl.display_contents(bowl1)

Bowl.clear_storage(bowl1)

Bowl.store(bowl1, item1_1)

Bowl.store(bowl1, item1_2)

Bowl.remove_item(bowl1)

Bowl.consume(bowl1)
