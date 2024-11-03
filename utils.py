def assert_this(result, expected):
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

    try:
        assert result == expected
        print(f'{GREEN}PASSED{RESET}')
    except AssertionError:
        print(f'{RED}FAILED: {result=}, {expected=}{RESET}')