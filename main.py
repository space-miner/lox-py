import scanner

if __name__ == "__main__":
    tests = [
        "data.lox",
        "add.lox",
        "id.lox"
    ]
    for file_name in tests:
        sc = scanner.Scanner("./tests/"+file_name)
        sc.scan_tokens()
        tokens = [str(token) for token in sc.token_list]
        print(sc.source)
        print('\n'.join(tokens))
        print('\n')
