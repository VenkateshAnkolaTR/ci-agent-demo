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


# --- is_admin with non-dict inputs ---

def test_is_admin_with_list_returns_false():
    assert is_admin(["admin"]) is False


def test_is_admin_with_string_returns_false():
    assert is_admin("admin") is False


def test_is_admin_with_integer_returns_false():
    assert is_admin(42) is False


# --- get_user with unusual input types ---

def test_get_user_with_list_returns_none():
    assert get_user([1]) is None


def test_get_user_with_dict_returns_none():
    assert get_user({1: "user"}) is None


def test_get_user_with_very_large_id():
    assert get_user(10**18) is None


def test_get_user_with_negative_float_id():
    assert get_user(-1.5) is None


# --- User data completeness ---

def test_user_ids_are_unique():
    user1 = get_user(1)
    user2 = get_user(2)
    assert user1["name"] != user2["name"]


def test_user_roles_are_non_empty():
    for user_id in [1, 2]:
        user = get_user(user_id)
        assert user["role"] != ""


def test_known_users_are_not_admin():
    for user_id in [1, 2]:
        user = get_user(user_id)
        assert is_admin(user) is False
