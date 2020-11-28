import string
from itertools import combinations_with_replacement, combinations, permutations
import time
import csv
from security.utils import generate_random_string

alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

def brute_force(target, start_length, stop_length):
    for length in range(start_length, stop_length):
        for combi in combinations_with_replacement(alphabet, length):
            for perm in permutations(combi):
                current = ''.join(perm)
                if current == target: # TODO: check password with website/app/program directly
                    return True
    return False

CHARSETS = { string.ascii_lowercase: 'lower', string.ascii_uppercase: 'upper', string.digits: 'digits', string.punctuation: 'punctuation'}

def gen_pwd(length, charsets):
    password = generate_random_string(length, charsets)
    charsets_names = sorted(set(map(CHARSETS.get, charsets)))
    return { '_'.join(charsets_names) + f'_{length}': f'{password}' }

def gen_pwds(start_length, stop_length=None):
    assert start_length >= 4
    if not stop_length or stop_length < start_length:
        stop_length = start_length
    pwds = {}
    for length in range(start_length, stop_length + 1):
        for charsets_count in range(len(CHARSETS)):
            for charsets in combinations(CHARSETS.keys(), charsets_count+1):
                pwd = gen_pwd(length, charsets)
                pwds.update(pwd)
    return pwds

def build_results(path = "brute_force_results.csv"):
    pwds = gen_pwds(4, 25)
    with open(path, "a", newline='') as f:
        f.write('\n\n')
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['category', 'duration', 'password'])
        for category, password in pwds.items():
            print(category, end='')
            print(' -- ', end='')
            print(password, end='')
            start_time = time.time()
            assert brute_force(password, 4, 25)
            duration = time.time() - start_time
            print(f': {duration}s ({password})')
            writer.writerow([category, duration, password])

def main():
    build_results()

if __name__ == '__main__':
    main()