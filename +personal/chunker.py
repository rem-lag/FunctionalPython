

def make_chunks(item, batches):
    """
    Generator function
    Takes list (or other slicable) and returns it
    split into desired number of batches
    Batches will be of equal size, except last
    Last will include remainder of list items
    """
    item_len = len(item)
    base_size = item_len // batches
    add_final = item_len % batches
    
    def chunker(chunk, start, stop, remain):
        if remain == 1:
            yield chunk[start:stop+add_final]
            return
        yield chunk[start:stop]
        yield from chunker(chunk, start+base_size, stop+base_size, remain-1)
    
    return chunker(item, 0, base_size, batches)

def make_chunks_extra(item, batches):
    """
    Generator function
    Takes list (or other slicable) and returns it
    split into desired number of batches
    Remainder added to extra batch
    Batches will be of equal size, except extra
    """
    item_len = len(item)
    base_size = item_len // batches
    
    def chunker(chunk, start, stop, remain):
        if remain == 1:
            yield chunk[start:stop]
            yield chunk[stop:]
            return
        yield chunk[start:stop]
        yield from chunker(chunk, start+base_size, stop+base_size, remain-1)
    
    return chunker(item, 0, base_size, batches)

def main():
    list_one = [i for i in range(12)]
    list_two = [i for i in range(26)]
    list_three = [i for i in range(43)]
    list_test = [i for i in range(5,39)]


    batch_one = make_chunks(list_one, 6)
    batch_two = make_chunks(list_two, 4)
    batch_three = make_chunks(list_three, 8)
    batch_three_ex = make_chunks_extra(list_three, 8)

    print(f'Batch One:\n\t{list(batch_one)}')
    print(f'Batch Two:\n\t{list(batch_two)}')
    print(f'Batch Three:\n\t{list(batch_three)}\n\n')
    print(f'Batch Three Extra Method:\n\t{list(batch_three_ex)}\n\n')

    correct = [
        [5, 6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22],
        [23, 24, 25, 26, 27, 28],
        [29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
    ]

    correct_extra = [
        [5, 6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22],
        [23, 24, 25, 26, 27, 28],
        [29, 30, 31, 32, 33, 34],
        [35, 36, 37, 38]
    ]

    print('Batching using make_chunker\n')
    for i, batch in enumerate(make_chunks(list_test, 5)):
        try:
            assert batch == correct[i]
            print(f'\tBatch {i} - {batch}\tsize: {len(batch)}')
        except AssertionError:
            print(f"\tbatch {i} assertion failed!")
            print(f'\tthese items are not equal!\n\tGiven:   {batch}\n\tCorrect: {correct[i]}')

    print('\nBatching using make_chunks_extra\n')
    for i, batch in enumerate(make_chunks_extra(list_test, 5)):
        try:
            assert batch == correct_extra[i]
            print(f'\tBatch {i} - {batch}\tsize: {len(batch)}')
        except AssertionError:
            print(f"\tbatch {i} assertion failed!")
            print(f'\tthese items are not equal!\n\tGiven:   {batch}\n\tCorrect: {correct_extra[i]}')


if __name__ == '__main__':
    main()
        