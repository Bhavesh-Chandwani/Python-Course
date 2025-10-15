def display_user_info(**user_details):
    print(f"The arguments are of type: {type(user_details)}")
    for key, value in user_details.items():
        print(f"{key}: {value}")

display_user_info(username="Alex", status="Active")