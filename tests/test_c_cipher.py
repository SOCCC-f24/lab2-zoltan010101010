import pytest
import logging
from src.c_cipher import encrypt, decrypt

def test_kick_the_front_tire():
    assert encrypt() == 'dbc012'

def test_encrypt_length_error(caplog):
    """Test that a length error message is logged for invalid email size"""
    with caplog.at_level(logging.INFO):
        result = encrypt("abcd1234")
    assert "Length check failed" in caplog.text
    assert "Email must be 6 characters long." in caplog.text
    assert result == "Length check failed\nEmail must be 6 characters long."
    
def test_encrypt_alphanumeric_error(caplog):
    """Test that an alphanumeric error message is logged for invalid email format"""
    with caplog.at_level(logging.INFO):
        result = encrypt("abc1@3")
    assert "alpha num check failed" in caplog.text
    assert "Email must have 3 letters followed by 3 digits." in caplog.text
    assert result == "alpha num check failed\nEmail must have 3 letters followed by 3 digits."

def test_successful_encryption(caplog):
    """Test that the email is encrypted correctly"""
    result = encrypt("abc012")
    assert result == "def345"
    assert "def345" not in caplog.text 

'''
def test_kick_the_back_tire():
    assert decrypt() == 'aef345'

def test_decrypt_length_error(caplog):
    """Test that a length error message is logged for invalid email size"""
    with caplog.at_level(logging.INFO):
        result = decrypt("defg456")  # Updated function call
    assert "Length check failed" in caplog.text
    assert "Email must be 6 characters long." in caplog.text
    assert result == "Length check failed\nEmail must be 6 characters long."

def test_decrypt_alphanumeric_error(caplog):
    """Test that an alphanumeric error message is logged for invalid email format"""
    with caplog.at_level(logging.INFO):
        result = decrypt("def4%6")  # Updated function call
    assert "alpha num check failed" in caplog.text
    assert "Email must have 3 letters followed by 3 digits." in caplog.text
    assert result == "alpha num check failed\nEmail must have 3 letters followed by 3 digits."

def test_successful_decryption(caplog):
    """Test that the email is encrypted correctly"""
    result = decrypt("def345")
    assert result == "abc012"
    assert "abc012" not in caplog.text 
'''
