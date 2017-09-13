

def decode():
    code_dict = {i: chr(i) for i in range(256)}

    res = ''

    with open('/home/erupeika/Desktop/compressedfile3.z', 'rb') as file:

        bin_buffer_str = ''
        conjecture = ''

        byte = file.read(1)
        while byte != b'':
            bin_byte_str = bin(int.from_bytes(byte, 'big'))[2:].zfill(8)
            bin_buffer_str += bin_byte_str

            if (len(bin_buffer_str) >= 12):
                code_int = int(bin_buffer_str[:12], 2)
                bin_buffer_str = bin_buffer_str[12:]

                decoded_entry = code_dict[code_int]

                res += decoded_entry

#                 print(res)
#                 if res == 'It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith':
#                     print('lol')

                if (not conjecture):
                    # first iteration
                    conjecture = decoded_entry
                    continue

#                 if (conjecture+decoded_entry not in code_dict.values()):
                    # Output decoded entry and add a new entry to the code_dict

                code_dict[len(code_dict)] = conjecture+decoded_entry

                if (len(code_dict) == 4096):
                    print(res)
                    code_dict = {i: chr(i) for i in range(256)}

                conjecture = decoded_entry


            byte = file.read(1)

    print(res)

def main():
    decode()

if __name__ == "__main__":
    main()
