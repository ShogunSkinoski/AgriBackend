import numpy as np

class DetectionConstants:
    MIN_SCORE_THRESHOLD = 0.5
    LOWER_YELLOW_HSV_RANGE = np.array([19, 150, 50], np.uint8)
    UPPER_YELLOW_HSV_RANGE = np.array([29, 255, 255], np.uint8)
    BOX_KERNEL = np.ones((5,5), "uint8")
    BLACK_COLOR = [0, 0, 0]
    LEAF = "yaprak"
    FLOWER = "cicek"
    TOMATOUS = "domates"
    LEAF_LIGHT_COLOR = "yaprak_acik"
    LEAF_DARK_COLOR = "yaprak_koyu"
    FLOWER_LIGHT_COLOR = "yaprak_acik"
    FLOWER_DARK_COLOR = "yaprak_koyu"