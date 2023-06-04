def sum_of_pieces(a, piece_length):
    sum = 0
    for i in a:
        sum += i // piece_length
    return sum


def solution(a, k):
    max_piece_length = max(a)
    min_piece_length = 1
    while min_piece_length < max_piece_length:
        piece_length = (max_piece_length + min_piece_length + 1) // 2
        no_of_pieces = sum_of_pieces(a, piece_length)
        if no_of_pieces >= k:
            min_piece_length = piece_length
        else:
            max_piece_length = piece_length - 1
    return piece_length


print(solution([4, 8, 4, 5, 3, 7, 1, 2, 6], 5))
