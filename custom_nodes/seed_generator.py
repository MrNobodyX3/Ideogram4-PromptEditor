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

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("seed",)
    FUNCTION = "generate_seed"
    CATEGORY = "utilities"

    def generate_seed(self, seed, mode, phrase=""):
        if mode == "fixed":
            return (seed,)
        elif mode == "random":
            return (random.randint(0, 0xffffffffffffffff),)
        elif mode == "step":
            return (seed + 1,)
        elif mode == "phrase":
            if not phrase:
                return (seed,)
            digest = hashlib.sha256(phrase.encode()).digest()
            value = int.from_bytes(digest[:8], byteorder="big")
            return (value,)
        return (seed,)


NODE_CLASS_MAPPINGS = {
    "SeedGenerator": SeedGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SeedGenerator": "Seed Generator"
}
