import os, pytest

TEST_PDF = os.path.join('Tests', 'Reinforcement_Learning_Inspired_Adjustment_Module(Test).pdf')

def test_testpdf_exists_or_skip():
    if not os.path.exists(TEST_PDF):
        pytest.skip(f"Companion test PDF not found at {TEST_PDF}. Skipping.")
    assert os.path.getsize(TEST_PDF) > 0, "Test PDF exists but is empty."
