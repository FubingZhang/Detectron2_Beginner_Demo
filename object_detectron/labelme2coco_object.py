import labelme2coco

# set directory that contains labelme annotations and image files
labelme_folder = "./plant-train1/"		# 图片与.json文件路径
# set path for coco json to be saved
save_json_path = "./plant_coco.json" # 保存路径
# convert labelme annotations to coco
labelme2coco.convert(labelme_folder, save_json_path)