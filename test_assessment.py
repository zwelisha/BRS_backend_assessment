import pytest
import assessment as asm

# Test character appearance count
def test_char_appearance_count():
    assert asm.char_appearance_count("Barrows", "r") == 2
    assert asm.char_appearance_count("Barrows", "b") == 1
    assert asm.char_appearance_count("Barrows", "B") == 1
    assert asm.char_appearance_count("Barrows", "c") == 0
    assert asm.char_appearance_count("Barrows", "a") == 1
    assert asm.char_appearance_count("Barrows", "w") == 1
    assert asm.char_appearance_count("Barrows", "s") == 1
