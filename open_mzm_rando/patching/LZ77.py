

MIN_MATCH_SIZE = 3
MAX_MATCH_SIZE = 18
MAX_WINDOW_SIZE = 0x1000

def find_longest_matches(input: bytes):
    length = len(input)
    triplets: dict[int, list[int]] = {}
    longest_matches: dict[int, list[int]] = {}

    for i in range(length-2):
        # get current triplet
        triplet = int.from_bytes(input[i:i+3], 'little')
        
        # if new triplet, add and continue at next idx
        if triplet not in triplets:
            triplets[triplet] = [i]
            continue

        window_start = max(i - MAX_WINDOW_SIZE, 0)
        max_size = min(MAX_MATCH_SIZE, length - i)
        longest_len = 0
        longest_idx = -1
        indexes = triplets[triplet]

        j = len(indexes) - 1
        if indexes[j] >= i - 1:
            j -= 1
        
        while j >= 0:
            idx = indexes[j]
            if idx < window_start:
                break

            match_len = MIN_MATCH_SIZE
            while match_len < max_size:
                if input[idx + match_len] != input[i + match_len]:
                    break
                match_len += 1
            
            if match_len > longest_len:
                longest_len = match_len
                longest_idx = idx

                if longest_len == max_size:
                    break
            
            j -= 1
        
        indexes.append(i)
        if longest_len >= MIN_MATCH_SIZE:
            longest_matches[i] = [longest_len, longest_idx]
    
    return longest_matches

def compress_LZ77(input: bytes) -> bytes:
    length = len(input)
    idx = 0
    longest_matches = find_longest_matches(input)

    output = bytearray()
    output.append(0x10)
    output.extend(length.to_bytes(3, 'little'))

    while idx < length:
        flag = len(output)
        output.append(0x0)

        for i in range(8):
            if idx in longest_matches:
                match = longest_matches[idx]
                match_offset = idx - match[1] - 1
                output.append(((match[0] - 3) << 4 | (match_offset >> 8)))
                output.append(match_offset % 256)
                output[flag] |= (0x80 >> i)
                idx += match[0]
            else:
                output.append(input[idx])
                idx += 1
            
            if idx >= length:
                return bytes(output)
    
    raise ValueError("LZ77 compression error")

def decompress_LZ77(input: bytes, idx: int) -> bytes:
    if input[idx] != 0x10:
        raise ValueError("LZ77-compressed data must start with 0x10!")
    
    remaining = int.from_bytes(input[idx+1:idx+4], 'little')
    output = bytearray(remaining)

    if remaining == 0:
        return 0
    
    src_start = idx
    idx += 4
    dst = 0

    while remaining > 0:
        cflag = input[idx]
        idx += 1

        for i in range(8):
            if cflag & 0x80 == 0:
                # uncompressed
                output[dst] = input[idx]
                dst += 1
                idx += 1
                remaining -= 1
            else:
                # compressed
                to_copy = (input[idx] >> 4) + MIN_MATCH_SIZE
                window = ((input[idx] & 0xF) << 8) + input[idx + 1] + 1
                idx += 2
                remaining -= to_copy

                for j in range(to_copy):
                    output[dst] = output[dst - window]
                    dst += 1
            
            
            cflag = cflag << 1

            if remaining <= 0:
                return output
    return idx - src_start