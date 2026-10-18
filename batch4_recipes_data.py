# -*- coding: utf-8 -*-
"""
Merges Batch 4 Parts A and B into batch4_recipes_list
"""
from batch4_data_a import recipes_a
from batch4_data_b import recipes_b

batch4_recipes_list = recipes_a + recipes_b
print(f"Total Batch 4 recipes loaded: {len(batch4_recipes_list)}")
