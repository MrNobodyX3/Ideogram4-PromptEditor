import hashlib
import random


class SeedGenerator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "mode": (["fixed", "random", "step", "phrase"],),
            },
            "optional": {
                "phrase": ("STRING", {"default": "", "multiline": False}),
            }
        }

    RETURN_TYPES = ("INT", "STRING")
    RETURN_NAMES = ("seed", "seed_str")
    FUNCTION = "generate_seed"
    CATEGORY = "utilities"

    def generate_seed(self, seed, mode, phrase=""):
        if mode == "fixed":
            value = seed
        elif mode == "random":
            value = random.randint(0, 0xffffffffffffffff)
        elif mode == "step":
            value = seed + 1
        elif mode == "phrase":
            if not phrase:
                value = seed
            else:
                digest = hashlib.sha256(phrase.encode()).digest()
                value = int.from_bytes(digest[:8], byteorder="big")
        else:
            value = seed
        return (value, str(value))


NODE_CLASS_MAPPINGS = {
    "SeedGenerator": SeedGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SeedGenerator": "Seed Generator"
}
