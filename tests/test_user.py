from src.user_utils import get_user, is_admin

# --- get_user tests ---

def test_get_user():
    user = get_user(1)
    assert user["name"] == "Venkatesh"

def test_get_user_role():
    user = get_user(1)
    assert user["role"] == "developer"

def test_get_second_user():
    user = get_user(2)
    assert user["name"] == "Priya"
    assert user["role"] == "devops"

def test_unknown_user():
    assert get_user(99) is None

def test_get_user_zero_id():
    assert get_user(0) is None

def test_get_user_negative_id():
    assert get_user(-1) is None

# --- is_admin tests ---

def test_not_admin():
    user = get_user(1)
    assert is_admin(user) == False

def test_is_admin_with_none():
    assert is_admin(None) == False

def test_is_admin_with_empty_dict():
    assert is_admin({}) == False

def test_is_admin_with_admin_role():
    assert is_admin({"name": "Admin", "role": "admin"}) == True

def test_is_admin_with_no_role_key():
    assert is_admin({"name": "Test"}) == False

def test_devops_is_not_admin():
    user = get_user(2)
    assert is_admin(user) == False
