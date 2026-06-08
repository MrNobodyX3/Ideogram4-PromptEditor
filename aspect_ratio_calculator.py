import math

class AspectRatioCalculator:
    """
    A custom node for ComfyUI that calculates width and height based on an aspect ratio and a maximum size.
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ratio_x": ("INT", {"default": 16, "min": 1, "max": 8192, "step": 1}),
                "ratio_y": ("INT", {"default": 9, "min": 1, "max": 8192, "step": 1}),
                "max_size": ("INT", {"default": 2048, "min": 64, "max": 8192, "step": 8}),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "calculate_dimensions"

    CATEGORY = "utilities"

    def calculate_dimensions(self, ratio_x, ratio_y, max_size):
        if ratio_x > ratio_y:
            width = max_size
            height = math.ceil(max_size * (ratio_y / ratio_x))
        else:
            height = max_size
            width = math.ceil(max_size * (ratio_x / ratio_y))
            
        # Ensure dimensions are divisible by 8 for compatibility with some models
        width = (width // 8) * 8
        height = (height // 8) * 8

        return (width, height)

NODE_CLASS_MAPPINGS = {
    "AspectRatioCalculator": AspectRatioCalculator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AspectRatioCalculator": "Aspect Ratio Calculator"
}