from src.user_utils import get_user, is_admin

# --- Integration tests combining get_user and is_admin ---

def test_developer_is_not_admin():
    user = get_user(1)
    assert user is not None
    assert user["role"] == "developer"
    assert is_admin(user) is False

def test_devops_is_not_admin():
    user = get_user(2)
    assert user is not None
    assert user["role"] == "devops"
    assert is_admin(user) is False

def test_nonexistent_user_is_not_admin():
    user = get_user(999)
    assert user is None
    assert is_admin(user) is False

# --- Tests for user data integrity ---

def test_all_valid_users_have_name():
    for user_id in [1, 2]:
        user = get_user(user_id)
        assert "name" in user

def test_all_valid_users_have_role():
    for user_id in [1, 2]:
        user = get_user(user_id)
        assert "role" in user

def test_user_names_are_strings():
    for user_id in [1, 2]:
        user = get_user(user_id)
        assert isinstance(user["name"], str)

def test_user_roles_are_strings():
    for user_id in [1, 2]:
        user = get_user(user_id)
        assert isinstance(user["role"], str)

# --- Boundary tests for get_user ---

def test_get_user_with_string_id():
    assert get_user("1") is None

def test_get_user_with_none_id():
    assert get_user(None) is None

def test_get_user_with_float_id():
    assert get_user(1.5) is None


def test_get_user_with_boolean_true_matches_first_user():
    user = get_user(True)
    assert user is not None
    assert user["name"] == "Venkatesh"


def test_get_user_with_boolean_false_returns_none():
    assert get_user(False) is None


def test_is_admin_is_case_sensitive():
    assert is_admin({"name": "Case", "role": "Admin"}) is False


def test_is_admin_with_extra_fields_still_true_for_admin_role():
    user = {"name": "Root", "role": "admin", "team": "platform", "active": True}
    assert is_admin(user) is True
