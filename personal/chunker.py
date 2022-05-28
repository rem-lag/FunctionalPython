

def make_chunks(item, batches):
    item_len = len(item)
    base_size = item_len//batches
    add_final = item_len%batches
    def chunker(chunk, start, stop, remain):
        yield chunk[start:stop]
        if remain == 0:
            yield chunk[start:stop+add_final]
            return
        yield from chunker(chunk, start+base_size, stop+base_size, remain-1)
    
    return chunker(item, 0, base_size, batches)

def main():
    list_one = [i for i in range(12)]
    list_two = [i for i in range(26)]
    list_three = [i for i in range(43)]

    batch_one = make_chunks(list_one, 6)
    batch_two = make_chunks(list_two, 4)
    batch_three = make_chunks(list_three, 8)

    print(f'Batch One:\n\t{batch_one}')
    print(f'Batch Two:\n\t{batch_two}')
    print(f'Batch Three:\n\t{batch_three}')


if __name__ == '__main__':
    main()
        