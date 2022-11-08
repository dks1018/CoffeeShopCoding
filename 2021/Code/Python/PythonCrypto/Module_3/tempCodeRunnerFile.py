rand_bytes = secrets.token_bytes(16)
    let_val = string.ascii_letters + string.digits
    secret_val = ''.join(secrets.choice(let_val) for i in range(16))
    random_key = os.urandom(16)

    key = rand_bytes