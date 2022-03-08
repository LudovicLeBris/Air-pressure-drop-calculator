from pathlib import Path

CUR_DIR = Path.cwd()

SHAPE: list = ["circular", "rectangular"]

ROUGHNESS: dict = {
    "galvanised steel": 10 * 10 ** -5,
    "aluminium": 0.2 * 10 ** -5,
    "steel": 5 * 10 ** -5,
    "cast iron": 20 * 10 ** -5,
    "plastic": 0.2 * 10 ** -5,
    "smooth concrete": 30 * 10 ** -5,
    "ordinary concrete": 100 * 10 ** -5,
    "brick": 200 * 10 ** -5,
    "terracotta": 500 * 10 ** -5
}

STD_CIRCULAR_DIAMETER: list = [80, 160, 200, 250, 315, 355, 400, 450, 500, 560, 630, 710, 800, 900, 1000, 1250]

SING_CIRC: dict = {
    '90_elbow': [
        0,
        0.4,
        '90° circular elbow'
    ],
    "30_elbow": [
        0,
        0.17,
        "30° circular elbow"
    ],
    "45_elbow": [
        0,
        0.23,
        "45° circular elbow"
    ],
    "60_elbow": [
        0,
        0.31,
        "60° circular elbow"
    ],
    "90_sharp_elbow": [
        0,
        1.2,
        "90° circular sharp elbow"
    ],
    "30_sharp_elbow": [
        0,
        0.16,
        "30° circular sharp elbow"
    ],
    "45_sharp_elbow": [
        0,
        0.32,
        "45° circular sharp elbow"
    ],
    "60_sharp_elbow": [
        0,
        0.56,
        "60° circular sharp elbow"
    ],
    "90_sep_tee": [
        0,
        2.0,
        "90° separation tee"
    ],
    "90_junc_tee": [
        0,
        2.27,
        "90° junction tee"
    ],
    "45_sep_tee": [
        0,
        0.58,
        "45° separation tee"
    ],
    "45_junc_tee": [
        0,
        1.64,
        "45° junction tee"
    ],
    "pressed_reducer": [
        0,
        0.35,
        "pressed circular reducer"
    ],
    "long_reducer": [
        0,
        0.59,
        "long circular reducer"
    ]
}

SING_RECT: dict = {
    "90_elbow": [
        0,
        0.36,
        "90° rectangular elbow"
    ],
    "30_elbow": [
        0,
        0.15,
        "30° rectangular elbow"
    ],
    "45_elbow": [
        0,
        0.21,
        "45° rectangular elbow"
    ],
    "60_elbow": [
        0,
        0.28,
        "60° rectangular elbow"
    ],
    "90_sharp_elbow": [
        0,
        1.28,
        "90° rectangular sharp elbow"
    ],
    "30_sharp_elbow": [
        0,
        0.17,
        "30° rectangular sharp elbow"
    ],
    "45_sharp_elbow": [
        0,
        0.34,
        "45° rectangular sharp elbow"
    ],
    "60_sharp_elbow": [
        0,
        0.59,
        "60° rectangular sharp elbow"
    ],
    "90_sep_tee": [
        0,
        2.0,
        "90° separation tee"
    ],
    "90_junc_tee": [
        0,
        2.27,
        "90° junction tee"
    ],
    "45_sep_tee": [
        0,
        0.58,
        "45° separation tee"
    ],
    "45_junc_tee": [
        0,
        1.64,
        "45° junction tee"
    ],
    "pressed_reducer": [
        0,
        0.35,
        "pressed rectangular reducer"
    ],
    "long_reducer": [
        0,
        0.08,
        "long rectangular reducer"
    ]
}


def equiv_diameter(height: int, width: int) -> float:
    """
    Calculation of the circular equivalent diameter for a rectangular shape.

    Args:
        height (int):
            Height of the rectangle
        width (int):
            Width of the rectangle
    Returns:
        Equivalent diameter value rounded to 3 decimal places.
    """
    equiv_diam = (1.265 * (height * width) ** 0.6) / (height + width) ** 0.2
    return round(equiv_diam, 3)
