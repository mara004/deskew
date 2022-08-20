import os

import pytest
from skimage import io

from deskew import determine_skew


@pytest.mark.parametrize(
    "image,expected_angle",
    [
        ("1", pytest.approx(-1.0, abs=0.01)),
        ("2", pytest.approx(-2.0, abs=0.01)),
        ("3", pytest.approx(-6.0, abs=0.01)),
        ("4", pytest.approx(7.0, abs=0.01)),
        ("5", pytest.approx(3.0, abs=0.01)),
        ("6", pytest.approx(-3.0, abs=0.01)),
        ("7", pytest.approx(3.0, abs=0.01)),
        ("8", pytest.approx(15.0, abs=0.01)),
    ],
)
def test_deskew(image, expected_angle):
    root_folder = f"results/{image}"
    if not os.path.exists(root_folder):
        os.makedirs(root_folder)

    image = io.imread(os.path.join(os.path.dirname(__file__), f"deskew-{image}.png"))
    angle = determine_skew(image)
    print(angle - expected_angle.expected)
    assert angle == expected_angle
    assert False


@pytest.mark.parametrize(
    "image,expected_angle",
    [
        ("1", pytest.approx(-1.4, abs=0.01)),
        ("2", pytest.approx(-2.1, abs=0.01)),
        ("3", pytest.approx(-6.3, abs=0.11)),
        ("4", pytest.approx(7.0, abs=0.01)),
        ("5", pytest.approx(3.4, abs=0.01)),
        ("6", pytest.approx(-2.8, abs=0.01)),
        ("7", pytest.approx(3.7, abs=0.01)),
        ("8", pytest.approx(14.9, abs=0.01)),
    ],
)
def test_deskew_higher_pressision(image, expected_angle):
    root_folder = f"results/{image}"
    if not os.path.exists(root_folder):
        os.makedirs(root_folder)

    image = io.imread(os.path.join(os.path.dirname(__file__), f"deskew-{image}.png"))
    angle = determine_skew(image, num_angles=1800)
    print(angle - expected_angle.expected)
    assert angle == expected_angle
    assert False
