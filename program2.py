def decode_message(secret_message, decoder_key):
    def match_helper(secret_idx, key_idx):
        if secret_idx == len(secret_message) and key_idx == len(decoder_key):
            return True
        if secret_idx == len(secret_message) or key_idx == len(decoder_key):
            return False

        if decoder_key[key_idx] == "?":
            return match_helper(secret_idx + 1, key_idx + 1)
        elif decoder_key[key_idx] == "*":
            return match_helper(secret_idx + 1, key_idx) or match_helper(secret_idx, key_idx + 1)
        else:
            return secret_message[secret_idx] == decoder_key[key_idx] and match_helper(secret_idx + 1, key_idx + 1)

    return match_helper(0, 0)


print(decode_message("aa", "a"))
print(decode_message("aa", "*"))  
print(decode_message("cb", "?a"))
