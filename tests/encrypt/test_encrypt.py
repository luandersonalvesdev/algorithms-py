import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("queijo", "a")

        encrypt_message(0, 3)

    assert encrypt_message("queijo", 10) == "ojieuq"

    assert encrypt_message("queijo", 2) == "ojie_uq"

    assert encrypt_message("queijo", 3) == "euq_oji"


# def test_encrypt_message_error_invalid_message():
#     with pytest.raises(TypeError, match='tipo inválido para message'):
#         encrypt_message(0, 3)

# def test_encrypt_message_key_bigger_than_message():
#     assert encrypt_message('queijo', 10) == 'ojieuq'

# def test_encrypt_message_return_inverse_string_odd_number():
#     assert encrypt_message('queijo', 2) == 'ojie_uq'

# def test_encrypt_message_return_inverse_string():
#     assert encrypt_message('queijo', 3) == 'euq_oji'
