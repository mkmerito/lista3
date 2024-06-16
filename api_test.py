import subprocess
import json

endpoints = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/users/1",
    "https://jsonplaceholder.typicode.com/todos/1"
]


def send_request(endpoint):
    result = subprocess.run(["curl", "-s", endpoint], capture_output=True, text=True)
    return result.stdout, result.returncode


def check_response(response):
    try:
        data = json.loads(response)
    except json.JSONDecodeError:
        return False, "Invalid JSON"

    if ("id") in data:
        return True, "PASSED"
    else:
        return False, "FAILED"


def main():
    for i, endpoint in enumerate(endpoints, start=1):
        response, status_code = send_request(endpoint)
        if status_code == 0:
            is_valid, message = check_response(response)
            print(f"Test {i}: {message}")
        else:
            print(f"Test {i}: FAILED to fetch the endpoint")


if __name__ == "__main__":
    main()
