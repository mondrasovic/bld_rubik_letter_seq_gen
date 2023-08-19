import random
import heapq

EDGES = (
    ("A", "R"),
    ("C", "I"),
    ("D", "E"),
    ("F", "L"),
    ("G", "Z"),
    ("H", "S"),
    ("J", "P"),
    ("K", "V"),
    ("N", "U"),
    ("O", "W"),
    ("T", "Y"),
)
CORNERS = (
    ("B", "N", "R"),
    ("C", "J", "M"),
    ("D", "F", "I"),
    ("G", "L", "V"),
    ("H", "T", "Z"),
    ("U", "O", "Y"),
    ("K", "P", "W"),
)

def generate_letter_sequence(pieces, repeat_prob=0.2):
    pieces_queue = [(random.random(), piece) for piece in pieces]
    heapq.heapify(pieces_queue)

    prev_piece = None
    while pieces_queue:
        _, current_piece = heapq.heappop(pieces_queue)
        if (not prev_piece) or (current_piece != prev_piece):
            yield random.choice(current_piece)
            prev_piece = current_piece
        if random.random() < repeat_prob:
            heapq.heappush(pieces_queue, (random.random(), current_piece))

def main():
    print(" - ".join(generate_letter_sequence(EDGES)))
    print(" - ".join(generate_letter_sequence(CORNERS)))

if __name__ == "__main__":
    main()
