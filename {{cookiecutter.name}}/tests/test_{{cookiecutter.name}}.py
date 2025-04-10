# Sample test suite to show different scenarios of testing async methods
import pytest
from aioresponses import aioresponses
from {{ cookiecutter.name }} import my_func

@pytest.mark.asyncio()
@pytest.mark.parametrize("name,expected", [
    ("Alice", "Hello, Alice!"),
    ("Bob", "Hello, Bob!"),
    ("Charlie", "Hello, Charlie!"),
])
async def test_remote_api(name, expected):
    with aioresponses() as mock:
        mock.get(
            f"https://example.com/api.json?name={name}",
            payload={"message": f"Hello, {name}!"},
            status=200,
        )
        resp = await my_func(name)
        assert resp == expected
