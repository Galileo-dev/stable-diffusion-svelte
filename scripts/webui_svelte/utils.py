import yaml
import os
import posixpath
from typing import List, Optional

# Taken from gradio repo
def safe_join(directory: str, path: str) -> Optional[str]:
    """Safely path to a base directory to avoid escaping the base directory.
    Borrowed from: werkzeug.security.safe_join"""
    _os_alt_seps: List[str] = list(
        sep for sep in [os.path.sep, os.path.altsep] if sep is not None and sep != "/"
    )

    if path != "":
        filename = posixpath.normpath(path)

    if (
        any(sep in filename for sep in _os_alt_seps)
        or os.path.isabs(filename)
        or filename == ".."
        or filename.startswith("../")
    ):
        return None
    return posixpath.join(directory, filename)


# Taken from krita


def load_config():
    with open("./config.yaml") as file:
        return yaml.safe_load(file)

def save_img(image, sample_path, filename):
    path = os.path.join(sample_path, filename)
    image.save(path)
    return os.path.abspath(path)

def fix_aspect_ratio(base_size, max_size, orig_width, orig_height):
    def rnd(r, x):
        z = 64
        return z * round(r * x / z)

    ratio = orig_width / orig_height

    if orig_width > orig_height:
        width, height = rnd(ratio, base_size), base_size
        if width > max_size:
            width, height = max_size, rnd(1 / ratio, max_size)
    else:
        width, height = base_size, rnd(1 / ratio, base_size)
        if height > max_size:
            width, height = rnd(ratio, max_size), max_size

    new_ratio = width / height

    print(f"img size: {orig_width}x{orig_height} -> {width}x{height}, "
          f"aspect ratio: {ratio:.2f} -> {new_ratio:.2f}, {100 * (new_ratio - ratio) / ratio :.2f}% change")
    return width, height

def collect_prompt(opt):
    prompts = opt['prompts']
    if isinstance(prompts, str):
        return prompts
    if isinstance(prompts, list):
        return ", ".join(prompts)
    if isinstance(prompts, dict):
        prompt = ""
        for item, weight in prompts.items():
            if not prompt == "":
                prompt += " "
            if weight is None:
                prompt += f"{item}"
            else:
                prompt += f"{item}:{weight}"
        return prompt
    raise Exception("wtf man, fix your prompts")

