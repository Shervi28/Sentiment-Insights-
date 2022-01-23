def delete_line():
    with open('data.txt', 'r') as f:
        with open('new.txt', 'w') as w:
            for line in f:
                if line.strip():
                    w.write(line)