

def make_chunks(item, batches):
    """
    Generator function
    Takes list (or other slicable) and returns it
    split into desired number of batches
    Batches will be of equal size, except last
    Last will include remainder of list items
    """
    item_len = len(item)
    base_size = item_len//batches
    add_final = item_len%batches
    def chunker(chunk, start, stop, remain):
        if remain == 1:
            yield chunk[start:stop+add_final]
            return
        yield chunk[start:stop]
        yield from chunker(chunk, start+base_size, stop+base_size, remain-1)
    
    return chunker(item, 0, base_size, batches)

def main():
    list_one = [i for i in range(12)]
    list_two = [i for i in range(26)]
    list_three = [i for i in range(43)]

    batch_one = make_chunks(list_one, 6)
    batch_two = make_chunks(list_two, 4)
    batch_three = make_chunks(list_three, 8)

    print(f'Batch One:\n\t{list(batch_one)}')
    print(f'Batch Two:\n\t{list(batch_two)}')
    print(f'Batch Three:\n\t{list(batch_three)}')


if __name__ == '__main__':
    main()
        